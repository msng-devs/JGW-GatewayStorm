from fastapi.requests import Request
from fastapi import APIRouter, Depends
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.curd.service import findAll
from app.core.db import get_db

path_view_route = APIRouter()

templates = Jinja2Templates(directory="./resources/templates/")


@path_view_route.get("/path/{path_id}", response_class=HTMLResponse)
async def paths(path_id:int ,request: Request, db=Depends(get_db)):
    # list_service = findAll(db)
    #
    # list_response = []
    #
    # for service in list_service:
    #     list_response.append(
    #         {
    #             "id": service.SERVICE_PK,
    #             "name": service.SERVICE_NM,
    #             "index": service.SERVICE_INDEX,
    #             "domain": service.SERVICE_DOMAIN
    #         }
    #     )

    return templates.TemplateResponse("path.html", {"request": request})
