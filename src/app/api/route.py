from fastapi import APIRouter
from src.app.api.ping import ping_route
from src.app.api.v1.endpoints.path import path_route
from src.app.api.v1.endpoints.service import service_route
from src.app.api.v1.endpoints.auth import auth_route

api_route = APIRouter()
api_route.include_router(ping_route)
api_route.include_router(service_route)
api_route.include_router(path_route)
api_route.include_router(auth_route)