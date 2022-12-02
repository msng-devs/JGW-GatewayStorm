import bcrypt
from fastapi import APIRouter,Response

from app.auth.auth import load_user, manager
from app.schemas.auth import LoginReqeust
from datetime import timedelta
from app.utlis.exceptions import NotValidUserIdOrPw

auth_route = APIRouter(prefix="/api/v1/auth", tags=["auth"])


@auth_route.post("")
async def login(response: Response, req: LoginReqeust):
    id = req.id
    pw = req.pw

    user = load_user(id)

    if not user:
        raise NotValidUserIdOrPw
    elif bcrypt.checkpw(bytes(pw, "utf-8"), user[id]['password']):
        raise NotValidUserIdOrPw

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