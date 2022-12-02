from fastapi import APIRouter
from app.api.ping import ping_route
from app.api.v1.endpoints.path import path_route
from app.api.v1.endpoints.service import service_route
from app.api.v1.endpoints.auth import auth_route
from app.api.v1.endpoints.refresh import refresh_router

api_route = APIRouter()
api_route.include_router(ping_route)
api_route.include_router(service_route)
api_route.include_router(path_route)
api_route.include_router(auth_route)
api_route.include_router(refresh_router)