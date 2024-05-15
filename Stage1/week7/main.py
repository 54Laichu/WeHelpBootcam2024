import os
from dotenv import load_dotenv
import json
from fastapi import FastAPI, Request, Form, status, Body
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from typing import Annotated
import mysql.connector

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# connect DB
load_dotenv()
db = mysql.connector.connect(
    host=os.environ['DB_HOST'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'],
    database=os.environ['DB_NAME']
)

# load error messages
with open("data/error_messages.json", "r") as file:
    ERROR_MESSAGES = json.load(file)

# routing
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/error", response_class=HTMLResponse)
async def error(request: Request, message: str):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})

@app.get("/member", response_class=HTMLResponse)
async def member(request: Request):
    if "member_id" not in request.session:
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

    cursor = db.cursor()
    query = "SELECT member.id, member.username, message.id, message.content FROM message JOIN member ON message.member_id = member.id ORDER BY message.time DESC"
    cursor.execute(query)
    messages = cursor.fetchall()
    cursor.close()

    return templates.TemplateResponse("member.html", {"request": request, "messages": messages})


@app.post("/signin")
async def signin(request: Request, username: Annotated[str, Form(...)], password: Annotated[str, Form(...)]):
    if not username or not password:
        return RedirectResponse(url=f"/error?message={ERROR_MESSAGES['missing_fields']}", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        cursor = db.cursor()
        query = "SELECT * FROM member WHERE username = %s AND password = %s"
        values = (username, password)
        cursor.execute(query, values)
        member = cursor.fetchone()
        cursor.close()
        if member:
            request.session["member_id"] = member[0]
            request.session["member_username"] = member[2]
            request.session["member_name"] = member[1]
            return RedirectResponse(url="/member", status_code=status.HTTP_303_SEE_OTHER)
        else:
            return RedirectResponse(url=f"/error?message={ERROR_MESSAGES['invalid_credentials']}", status_code=status.HTTP_303_SEE_OTHER)

@app.post("/signup")
async def signup(request: Request, name: Annotated[str, Form(...)], username: Annotated[str, Form(...)], password: Annotated[str, Form(...)]):
    if not name or not username or not password:
        return RedirectResponse(url=f"/error?message={ERROR_MESSAGES['missing_fields']}", status_code=status.HTTP_303_SEE_OTHER)
    else:
        cursor = db.cursor()
        query = "SELECT * FROM member WHERE username = %s"
        values = (username,)
        cursor.execute(query, values)
        existing_member = cursor.fetchone()
        if existing_member:
            cursor.close()
            return RedirectResponse(url=f"/error?message={ERROR_MESSAGES['repeated_username']}", status_code=status.HTTP_303_SEE_OTHER)
        else:
            query = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
            values = (name, username, password)
            cursor.execute(query, values)
            db.commit()
            cursor.close()
            return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/signout")
async def signout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/api/member")
async def api_member(request: Request, username: str = None):
    if username:
        cursor = db.cursor()
        query = "SELECT * FROM member WHERE username = %s"
        values = (username,)
        cursor.execute(query, values)
        member = cursor.fetchone()
        cursor.close()

        if not member:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"data": None})

        return JSONResponse(status_code=status.HTTP_200_OK, content={"data": {"id": member[0], "name": member[1], "username": member[2]}})
    else:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"data": None})

@app.patch("/api/member")
async def update_member_name(request: Request, body: dict = Body(...)):
    if "member_id" not in request.session:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"error": True})

    member_id = request.session["member_id"]
    name = body.get("name")

    if not name:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": True})

    cursor = db.cursor()
    query = "UPDATE member SET name = %s WHERE id = %s"
    values = (name, member_id)

    try:
        cursor.execute(query, values)
        db.commit()
        return JSONResponse(status_code=status.HTTP_200_OK, content={"ok": True})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": True})
    finally:
        cursor.close()
