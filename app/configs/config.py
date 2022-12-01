import app.configs.secret as secret
from pydantic import BaseSettings
from functools import lru_cache
import bcrypt

class Settings(BaseSettings):
    PROFILE = str = 'local'
    INIT_USER_NM = 'admin'
    INIT_USER_ID = 'heroes'
    INIT_USER_PW = 'sigong'

    if PROFILE == 'local':
        APP_NAME = 'GatewayStorm'
        CONFIG_NM = "local"

        #Database Setup
        DB_HOST = secret.DB_HOST
        DB_USER_NM = secret.DB_USER_NM
        DB_USER_PW = secret.DB_USER_PW
        DB_NAME = secret.DB_NAME

        #Auth Setup
        AUTH_SECRET_KEY = secret.AUTH_SECRET_KEY
        USER_NM = INIT_USER_NM
        USER_ID = INIT_USER_ID
        USER_PW = bcrypt.hashpw(password=bytes(INIT_USER_PW, 'utf-8'), salt=bcrypt.gensalt())

        GATEWAY_DOMAIN = secret.GATEWAY_DOMAIN

    elif PROFILE == 'test':
        CONFIG_NM = "test"
        DB_HOST = secret.DB_HOST
        DB_USER_NM = secret.DB_USER_NM
        DB_USER_PW = secret.DB_USER_PW
        DB_NAME = secret.DB_NAME

        # Auth Setup
        AUTH_SECRET_KEY = secret.AUTH_SECRET_KEY
        USER_NM = INIT_USER_NM
        USER_ID = INIT_USER_ID
        USER_PW = bcrypt.hashpw(password=bytes(INIT_USER_PW, 'utf-8'), salt=bcrypt.gensalt())

        GATEWAY_DOMAIN = secret.GATEWAY_DOMAIN

    elif PROFILE == 'product':
        CONFIG_NM = "product"
        DB_HOST = secret.DB_HOST
        DB_USER_NM = secret.DB_USER_NM
        DB_USER_PW = secret.DB_USER_PW
        DB_NAME = secret.DB_NAME

        # Auth Setup
        AUTH_SECRET_KEY = secret.AUTH_SECRET_KEY
        USER_NM = INIT_USER_NM
        USER_ID = INIT_USER_ID
        USER_PW = bcrypt.hashpw(password=bytes(INIT_USER_PW, 'utf-8'), salt=bcrypt.gensalt())

        GATEWAY_DOMAIN = secret.GATEWAY_DOMAIN

@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()