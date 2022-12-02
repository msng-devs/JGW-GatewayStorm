from fastapi import APIRouter, Depends

from app.auth.auth import manager
from app.core.db import get_db
from app.crud.path import pathAdd, pathUpdate, pathDelete
from app.core.model import Path
from app.schemas.path import PathAddRequest,PathUpdateRequest


path_route = APIRouter(prefix="/api/v1/path", tags=["path"])


@path_route.post("")
async def addPath(req: PathAddRequest, db=Depends(get_db),user=Depends(manager)):

    new_path = Path(**{
        "API_ROUTE_PATH": req.path,
        "METHOD_METHOD_PK": req.method_id,
        "SERVICE_SERVICE_PK": req.service_id
    })
    new_path.set_option(req.option, req.role_id if req.role_id is not None else None)
    pathAdd(db, new_path)

    return {"message": "ok"}


@path_route.put("/{path_id}")
async def updatePath(req: PathUpdateRequest, path_id: int, db=Depends(get_db),user=Depends(manager)):
    new_path = Path(**{
        "API_ROUTE_PATH": req.path,
        "METHOD_METHOD_PK": req.method_id})

    new_path.set_option(req.option, req.role_id if req.role_id is not None else None)
    pathUpdate(db, path_id, new_path)

    return {"message": "ok"}


@path_route.delete("/{path_id}")
async def deletePath(path_id: int, db=Depends(get_db),user=Depends(manager)):
    pathDelete(db, path_id)
    return {"message": "ok"}
