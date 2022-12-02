from fastapi_login import LoginManager
from src.app.configs.config import settings
from src.app.utlis.exceptions import NotAuthenticatedException

manager = LoginManager(settings.AUTH_SECRET_KEY, token_url='/api/v1/auth', use_cookie=True,use_header=False)
manager.not_authenticated_exception = NotAuthenticatedException


@manager.user_loader()
def load_user(id: str) -> dict | None:
    if id == settings.USER_ID:
        return {settings.USER_ID: {'password': settings.USER_PW}}
    return None
