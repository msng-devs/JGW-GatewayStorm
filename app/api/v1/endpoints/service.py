from fastapi import APIRouter, Depends

from app.core.db import get_db
from app.core.model import Service
from app.schemas.service import ServiceAddRequest
from app.curd.service import add,update,delete

service_route = APIRouter(prefix="/api/v1/service",tags=["service"])


@service_route.post("")
def add_new_service(req: ServiceAddRequest, db=Depends(get_db)):
    new_service = Service(**{"SERVICE_NM": req.name, "SERVICE_DOMAIN": req.domain, "SERVICE_INDEX": req.index})
    add(db, new_service)
    return {"message": "ok"}


@service_route.put("/{service_id}")
def update_service(service_id:int,req: ServiceAddRequest, db=Depends(get_db)):
    new_service = Service(**{"SERVICE_NM": req.name, "SERVICE_DOMAIN": req.domain, "SERVICE_INDEX": req.index})
    update(db, service_id,new_service)
    return {"message": "ok"}


@service_route.delete("/{service_id}")
def update_service(service_id:int,db=Depends(get_db)):
    delete(db,service_id)
    return {"message": "ok"}
