import json
from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from typing import Annotated

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="your_secret_key")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

with open("data/error_messages.json", "r") as file:
    ERROR_MESSAGES = json.load(file)
    @app.get("/", response_class=HTMLResponse)
    async def home(request: Request):
        return templates.TemplateResponse("home.html", {"request": request})

    @app.post("/signin")
    async def signin(request: Request, username: Annotated[str, Form(...)], password: Annotated[str, Form(...)]):
        if not username or not password:
            return RedirectResponse(url=f"/error?message={ERROR_MESSAGES['missing_fields']}", status_code=status.HTTP_400_BAD_REQUEST)

        if username == "test" and password == "test":
            request.session["SIGNED_IN"] = True
            return RedirectResponse(url="/member", status_code=status.HTTP_303_SEE_OTHER)
        else:
            return RedirectResponse(url=f"/error?message={ERROR_MESSAGES['invalid_credentials']}", status_code=status.HTTP_303_SEE_OTHER)

    @app.get("/member", response_class=HTMLResponse)
    async def member(request: Request):
        if not request.session.get("SIGNED_IN"):
            return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
        return templates.TemplateResponse("member.html", {"request": request})

    @app.get("/signout")
    async def signout(request: Request):
        request.session["SIGNED_IN"] = False
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

    @app.get("/error", response_class=HTMLResponse)
    async def error(request: Request, message: str):
        return templates.TemplateResponse("error.html", {"request": request, "message": message})
