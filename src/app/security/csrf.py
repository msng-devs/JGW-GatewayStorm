from fastapi_csrf_protect import CsrfProtect
from pydantic import BaseModel
from app.configs.config import settings, get_settings


class CsrfSettings(BaseModel):
    secret_key: str = get_settings().CSRF_KEY


@CsrfProtect.load_config
def get_csrf_config():
    return CsrfSettings()
