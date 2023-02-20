from fastapi import APIRouter

from app.view.index_view import index_view_route
from app.view.refresh_view import refresh_view_route
from app.view.service_view import service_view_route
from app.view.path_view import path_view_route
from app.view.login_view import login_view_route

view_route = APIRouter()
view_route.include_router(index_view_route)
view_route.include_router(service_view_route)
view_route.include_router(path_view_route)
view_route.include_router(login_view_route)
view_route.include_router(refresh_view_route)