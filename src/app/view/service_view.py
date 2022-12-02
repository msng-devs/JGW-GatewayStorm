from fastapi.requests import Request
from fastapi import APIRouter, Depends
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from src.app.auth.auth import manager
from src.app.configs.config import settings
from src.app.crud.service import findServiceAll
from src.app.core.db import get_db

service_view_route = APIRouter(tags=["view"])

templates = Jinja2Templates(directory="app/resources/templates/")


@service_view_route.get("/", response_class=HTMLResponse)
async def services(request: Request, db=Depends(get_db) ,user=Depends(manager)):
    list_service = findServiceAll(db)

    list_response = []

    for service in list_service:
        list_response.append(
            {
                "id": service.SERVICE_PK,
                "name": service.SERVICE_NM,
                "index": service.SERVICE_INDEX,
                "domain": service.SERVICE_DOMAIN
            }
        )

    return templates.TemplateResponse("service.html",
                                      {"request": request,
                                       "services": list_response,
                                       "gatewaypath":settings.GATEWAY_DOMAIN+"/api/v1/refresh",
                                      "firebasekey":settings.FIREBASE_API_KEY
    })
