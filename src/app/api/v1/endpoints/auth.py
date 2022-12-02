from fastapi import APIRouter, Response, HTTPException
from starlette import status

from app.auth.auth import load_user, manager, pwd_context
from app.schemas.auth import LoginReqeust
from datetime import timedelta

auth_route = APIRouter(prefix="/api/v1/auth", tags=["auth"])


@auth_route.post("")
async def login(response: Response, req: LoginReqeust):
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
    return {"message": "ok"}

@auth_route.delete("")
async def logout(response: Response):
    response.delete_cookie(key="access_token",httponly=True)
    response.delete_cookie(key="access-token", httponly=True)
    return {"message": "ok"}