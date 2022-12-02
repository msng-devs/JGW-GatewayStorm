from fastapi import APIRouter
from src.app.view.service_view import service_view_route
from src.app.view.path_view import path_view_route
from src.app.view.login_view import login_view_route

view_route = APIRouter()
view_route.include_router(service_view_route)
view_route.include_router(path_view_route)
view_route.include_router(login_view_route)