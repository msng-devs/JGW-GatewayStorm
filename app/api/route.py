from fastapi import APIRouter
from app.api.ping import ping_route
from app.api.v1.endpoints.path import path_route
from app.api.v1.endpoints.service import service_route

api_route = APIRouter()
api_route.include_router(ping_route)
api_route.include_router(service_route)
api_route.include_router(path_route)