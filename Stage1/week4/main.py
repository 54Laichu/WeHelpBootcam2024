from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse, ORJSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/signin")
async def signin(request: Request, username: Annotated[str, Form(...)], password: Annotated[str, Form(...)]):
    if not username or not password:
        return RedirectResponse(url="/error?message=Please enter username and password", status_code=status.HTTP_400_BAD_REQUEST)

    if username == "test" and password == "test":
        return RedirectResponse(url="/member", status_code=status.HTTP_302_FOUND)
    else:
        return RedirectResponse(url="/error?message=WrongInfo", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/member", response_class=HTMLResponse)
async def member(request: Request):
    return templates.TemplateResponse("member.html", {"request": request})

@app.get("/error", response_class=HTMLResponse)
async def error(request: Request):
    return templates.TemplateResponse("error.html", {"request": request})
