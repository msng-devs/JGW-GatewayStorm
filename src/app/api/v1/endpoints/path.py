from fastapi import APIRouter, Depends
from fastapi_csrf_protect import CsrfProtect
from starlette.requests import Request

from app.security.auth import manager
from app.core.db import get_db
from app.crud.path import pathAdd, pathUpdate, pathDelete
from app.core.model import Path
from app.schemas.path import PathAddRequest,PathUpdateRequest


path_route = APIRouter(prefix="/api/v1/path", tags=["path"])


@path_route.post("/")
async def addPath(request: Request,req: PathAddRequest, db=Depends(get_db),user=Depends(manager), csrf_protect:CsrfProtect = Depends()):

    csrf_token = csrf_protect.get_csrf_from_headers(request.headers)
    csrf_protect.validate_csrf(csrf_token)

    new_path = Path(**{
        "API_ROUTE_PATH": req.path,
        "METHOD_METHOD_PK": req.method_id,
        "SERVICE_SERVICE_PK": req.service_id,
        "ROUTE_OPTION_ROUTE_OPTION_PK" : req.option,
        "ROLE_ROLE_PK" : req.role_id if req.option == 4 else None
    })
    pathAdd(db, new_path)

    return {"message": "ok"}


@path_route.put("/{path_id}")
async def updatePath(request: Request,req: PathUpdateRequest, path_id: int, db=Depends(get_db),user=Depends(manager), csrf_protect:CsrfProtect = Depends()):
    csrf_token = csrf_protect.get_csrf_from_headers(request.headers)
    csrf_protect.validate_csrf(csrf_token)

    new_path = Path(**{
        "API_ROUTE_PATH": req.path,
        "METHOD_METHOD_PK": req.method_id,
        "ROUTE_OPTION_ROUTE_OPTION_PK" : req.option,
        "ROLE_ROLE_PK" : req.role_id if req.option == 4 else None})

    pathUpdate(db, path_id, new_path)

    return {"message": "ok"}


@path_route.delete("/{path_id}")
async def deletePath(request: Request,path_id: int, db=Depends(get_db),user=Depends(manager), csrf_protect:CsrfProtect = Depends()):
    csrf_token = csrf_protect.get_csrf_from_headers(request.headers)
    csrf_protect.validate_csrf(csrf_token)

    pathDelete(db, path_id)
    return {"message": "ok"}
