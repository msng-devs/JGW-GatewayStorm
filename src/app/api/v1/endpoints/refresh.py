from typing import Union

from fastapi import APIRouter, Header, HTTPException, Request

from app.configs.config import settings
from app.utlis.logger import logger

refresh_router = APIRouter(prefix="/gs/api/v1/refresh",tags=["refresh"])

@refresh_router.get("")
async def gateway_refresh(request: Request):

    if request.headers.get(user_pk) is None or request.headers.get(role_pk) is None:
        raise HTTPException(403)

    logger.info(f"{user_pk} refresh gateway")

    return {"message":"ok"}

