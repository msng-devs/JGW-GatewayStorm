import app.configs.secret as secret
from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    PROFILE = str = 'local'

    if PROFILE == 'local':
        APP_NAME = 'GatewayStorm'
        CONFIG_NM = "local"
        DB_HOST = secret.DB_HOST
        DB_USER_NM = secret.DB_USER_NM
        DB_USER_PW = secret.DB_USER_PW
        DB_NAME = secret.DB_NAME

    elif PROFILE == 'test':
        CONFIG_NM = "test"
        DB_HOST = secret.DB_HOST
        DB_USER_NM = secret.DB_USER_NM
        DB_USER_PW = secret.DB_USER_PW
        DB_NAME = secret.DB_NAME

    elif PROFILE == 'product':
        CONFIG_NM = "product"
        DB_HOST = secret.DB_HOST
        DB_USER_NM = secret.DB_USER_NM
        DB_USER_PW = secret.DB_USER_PW
        DB_NAME = secret.DB_NAME

@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()