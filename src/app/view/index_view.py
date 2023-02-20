
from fastapi import APIRouter, Depends
from starlette.responses import HTMLResponse, RedirectResponse

from app.security.auth import manager

index_view_route = APIRouter(tags=["view"])

@index_view_route.get("/", response_class=HTMLResponse)
async def index(user=Depends(manager)):

    return RedirectResponse(url='/service')
