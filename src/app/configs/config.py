import app.configs.secret as secret
from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    PROFILE = str = 'product'

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
        USER_ID = secret.USER_ID

        USER_PW = secret.USER_PW

        GATEWAY_DOMAIN = secret.GATEWAY_DOMAIN
        # firebase api key(admin sdk 아님!)
        FIREBASE_API_KEY = "AIzaSyDABK25W8JSK0fri173PaHTixd06N_1eUk"

    elif PROFILE == 'test':
        CONFIG_NM = "test"
        DB_HOST = secret.DB_HOST
        DB_USER_NM = secret.DB_USER_NM
        DB_USER_PW = secret.DB_USER_PW
        DB_NAME = secret.DB_NAME

        # Auth Setup
        AUTH_SECRET_KEY = secret.AUTH_SECRET_KEY
        USER_ID = secret.USER_ID

        USER_PW = secret.USER_PW

        GATEWAY_DOMAIN = secret.GATEWAY_DOMAIN
        # firebase api key(admin sdk 아님!)
        FIREBASE_API_KEY = "AIzaSyDABK25W8JSK0fri173PaHTixd06N_1eUk"

    elif PROFILE == 'product':
        CONFIG_NM = "product"
        DB_HOST = secret.DB_HOST
        DB_USER_NM = secret.DB_USER_NM
        DB_USER_PW = secret.DB_USER_PW
        DB_NAME = secret.DB_NAME

        # Auth Setup
        AUTH_SECRET_KEY = secret.AUTH_SECRET_KEY
        USER_ID = secret.USER_ID

        USER_PW = secret.USER_PW

        GATEWAY_DOMAIN = secret.GATEWAY_DOMAIN
        # firebase api key(admin sdk 아님!)
        FIREBASE_API_KEY = "AIzaSyDABK25W8JSK0fri173PaHTixd06N_1eUk"

@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()