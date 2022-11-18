from fastapi import APIRouter
from ping import ping_route
from v1.endpoints.path import path_route
from v1.endpoints.service import service_route

api_route = APIRouter()
api_route.include_router(ping_route)
api_route.include_router(service_route)
api_route.include_router(path_route)