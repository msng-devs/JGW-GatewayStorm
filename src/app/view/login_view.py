from fastapi.params import Cookie
from fastapi.requests import Request
from fastapi import APIRouter,Response
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates


login_view_route = APIRouter(tags=["view"])

templates = Jinja2Templates(directory="app/resources/templates/")


@login_view_route.get("/login", response_class=HTMLResponse)
async def services(request: Request):

    return templates.TemplateResponse("login.html", {"request": request})

