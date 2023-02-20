import logging

from fastapi import APIRouter, Response, HTTPException, Depends
from fastapi_csrf_protect import CsrfProtect
from starlette import status
from starlette.requests import Request
from starlette.responses import RedirectResponse

from app.security.auth import load_user, manager, pwd_context
from app.schemas.auth import LoginReqeust
from datetime import timedelta

auth_route = APIRouter(prefix="/api/v1/auth", tags=["security"])


@auth_route.post("")
async def login(request: Request,response: Response, req: LoginReqeust, csrf_protect: CsrfProtect = Depends()):
    csrf_token = csrf_protect.get_csrf_from_headers(request.headers)
    csrf_protect.validate_csrf(csrf_token)

    id = req.id
    pw = req.pw

    user = load_user(id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f'존재하지 않는 ID입니다.',
        )

    elif pwd_context.verify(pw, user[id]['password']):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f'비밀번호가 잘못되었습니다.',
        )

    token = manager.create_access_token(
        data=dict(sub=id), expires=timedelta(hours=24)
    )
    manager.set_cookie(response,token)
    logging.info("OK")
    return "ok"

@auth_route.delete("")
async def logout(request: Request,response: Response, csrf_protect:CsrfProtect = Depends()):
    csrf_token = csrf_protect.get_csrf_from_headers(request.headers)
    csrf_protect.validate_csrf(csrf_token)

    response.delete_cookie(key="access_token",httponly=True)
    response.delete_cookie(key="access-token", httponly=True)
    return "ok"