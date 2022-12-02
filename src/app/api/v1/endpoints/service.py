from fastapi import APIRouter, Depends

from app.auth.auth import manager
from app.core.db import get_db
from app.core.model import Service
from app.schemas.service import ServiceAddRequest,ServiceUpdateRequest
from app.crud.service import serviceAdd,serviceUpdate,serviceDelete

service_route = APIRouter(prefix="/api/v1/service",tags=["service"])


@service_route.post("")
async def add_new_service(req: ServiceAddRequest, db=Depends(get_db),user=Depends(manager)):
    new_service = Service(**{"SERVICE_NM": req.name, "SERVICE_DOMAIN": req.domain, "SERVICE_INDEX": req.index})
    serviceAdd(db, new_service)
    return {"message": "ok"}


@service_route.put("/{service_id}")
async def update_service(service_id:int,req: ServiceUpdateRequest, db=Depends(get_db),user=Depends(manager)):
    new_service = Service(**{"SERVICE_NM": req.name, "SERVICE_DOMAIN": req.domain, "SERVICE_INDEX": req.index})
    serviceUpdate(db, service_id, new_service)
    return {"message": "ok"}


@service_route.delete("/{service_id}")
async def update_service(service_id:int,db=Depends(get_db),user=Depends(manager)):
    serviceDelete(db, service_id)
    return {"message": "ok"}
