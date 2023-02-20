import logging

from fastapi.requests import Request
from fastapi import APIRouter, Depends
from fastapi_csrf_protect import CsrfProtect
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from app.security.auth import manager
from app.crud.service import findServiceAll
from app.core.db import get_db

service_view_route = APIRouter(tags=["view"])

templates = Jinja2Templates(directory="app/resources/templates/")


@service_view_route.get("/service", response_class=HTMLResponse)
async def services(request: Request, db=Depends(get_db), user=Depends(manager), csrf_protect: CsrfProtect = Depends()):
    list_service = findServiceAll(db)

    list_response_services = [{"id": service.SERVICE_PK,
                               "name": service.SERVICE_NM,
                               "index": service.SERVICE_INDEX,
                               "domain": service.SERVICE_DOMAIN} for service in list_service]

    csrf_token = csrf_protect.generate_csrf()
    return templates.TemplateResponse("service.html",
                                      {"request": request,
                                       "services": list_response_services,
                                       'csrf_token': csrf_token})
