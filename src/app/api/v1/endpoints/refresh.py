from typing import Union

from fastapi import APIRouter, Header, HTTPException, Request

from app.configs.config import settings
from app.utlis.logger import logger

refresh_router = APIRouter(prefix="gs/api/v1/refresh",tags=["refresh"])

@refresh_router.get("")
async def gateway_refresh(user_pk: Union[str, None] = Header(default=None),role_pk: Union[int, None] = Header(default=None)):

    if user_pk is None or role_pk is None:
        raise HTTPException(403)

    logger.info(f"{user_pk} refresh gateway")

    return {"message":"ok"}

