from fastapi.requests import Request
from fastapi import APIRouter, Depends
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.auth.auth import manager
from app.configs.config import settings
from app.crud.role import findRoleAll
from app.crud.method import findMethodAll
from app.crud.path import findPathAllByServiceID,findOptionAll
from app.core.db import get_db
from app.crud.service import findById

path_view_route = APIRouter(tags=["view"])

templates = Jinja2Templates(directory="app/resources/templates/")


@path_view_route.get("/path/{service_id}", response_class=HTMLResponse)
async def paths(service_id:int ,request: Request, db=Depends(get_db),user=Depends(manager)):

    service_name = findById(db,service_id).SERVICE_NM

    list_paths = findPathAllByServiceID(db,service_id)
    list_roles = findRoleAll(db)
    list_methods = findMethodAll(db)
    list_options = findOptionAll()

    list_response_path = [{"id": path.API_ROUTE_PK,
                           "method_name": path.method.METHOD_NM,
                           "role_name" : path.role.ROLE_NM if path.role != None else "-",
                           "option_name" : path.get_option(),
                           "path": path.API_ROUTE_PATH} for path in list_paths]

    list_response_roles = [{"id" : role.ROLE_PK,"name" : role.ROLE_NM} for role in list_roles]
    list_response_options = [{"name" : option} for option in list_options]
    list_response_methods = [{"id" : method.METHOD_PK,"name" : method.METHOD_NM} for method in list_methods]


    return templates.TemplateResponse("path.html", {
        "request": request,
        "service_id":service_id,
        "service_name": service_name,
        "options":list_response_options,
        "paths":list_response_path,
        "roles":list_response_roles,
        "methods":list_response_methods,
        "gatewaypath":settings.GATEWAY_DOMAIN + "/api/v1/refresh",
        "firebasekey":settings.FIREBASE_API_KEY
    })
