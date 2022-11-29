from fastapi import APIRouter, Depends

from app.core.db import get_db

service_route = APIRouter(prefix="/api/v1/service")

@service_route.get("")
def getAllService(db=Depends(get_db)):

