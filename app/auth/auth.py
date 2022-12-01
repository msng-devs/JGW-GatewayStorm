from fastapi_login import LoginManager
from app.configs.config import settings
from app.utlis.exceptions import NotAuthenticatedException

manager = LoginManager(settings.AUTH_SECRET_KEY, token_url='/api/v1/auth', use_cookie=True)
manager.not_authenticated_exception = NotAuthenticatedException


@manager.user_loader()
def load_user(id: str) -> dict | None:
    if id == settings.USER_ID:
        return {settings.USER_ID: {'password': settings.USER_PW}}
    return None
