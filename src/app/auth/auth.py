from fastapi_login import LoginManager
from passlib.context import CryptContext

from app.configs import secret
from app.configs.config import settings
from app.utlis.exceptions import NotAuthenticatedException

manager = LoginManager(settings.AUTH_SECRET_KEY, token_url='/api/v1/auth', use_cookie=True,use_header=False)
manager.not_authenticated_exception = NotAuthenticatedException

pwd_context = CryptContext(schemes=["bcrypt"])
user = {settings.USER_ID: {'password': settings.USER_PW}}

@manager.user_loader()
def load_user(id: str) -> dict | None:

    if id == settings.USER_ID:
        return user
    return None
