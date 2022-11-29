from fastapi.requests import Request
from fastapi import APIRouter, Depends
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

import pystache
from jinja2 import Template
from app.curd.service import findAll
from app.schemas.service import ServiceResponse
from app.core.db import get_db

view_route = APIRouter()

templates = Jinja2Templates(directory="./resources/templates/")
view_route.mount("/static", StaticFiles(directory="./resources/static"), name="static")

@view_route.get("/")
async def services(request: Request,db=Depends(get_db)):
    list_service = findAll(db)

    list_response = []

    for service in list_service:
        list_response.append(
            {
                "name": service.SERVICE_NM,
                "index": service.SERVICE_INDEX,
                "domain": service.SERVICE_DOMAIN
            }
        )



    return templates.TemplateResponse("service.html", {
  "request": request,
  "services" : list_response})