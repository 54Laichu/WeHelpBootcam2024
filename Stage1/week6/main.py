import json
from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from typing import Annotated
import mysql.connector

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

with open("data/error_messages.json", "r") as file:
    ERROR_MESSAGES = json.load(file)

# 建立資料庫連線
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="website"
)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/error", response_class=HTMLResponse)
async def error(request: Request, message: str):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})

@app.get("/member", response_class=HTMLResponse)
async def member(request: Request):
    return templates.TemplateResponse("member.html", {"request": request})

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
            return RedirectResponse(url=f"/error?message={ERROR_MESSAGES['invalid_credentials']}", status_code=status.HTTP_401_UNAUTHORIZED)

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
