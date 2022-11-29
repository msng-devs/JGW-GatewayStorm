import sys

import app.configs.secret as secret
from pydantic import BaseSettings

class Config(BaseSettings):
    APP_NAME = 'GatewayStorm'


class LocalConfig(Config):
    CONFIG_NM = "local"
    DB_HOST = secret.DB_HOST
    DB_USER_NM = secret.DB_USER_NM
    DB_USER_PW = secret.DB_USER_PW
    DB_NAME = secret.DB_NAME

class TestConfig(Config):

    CONFIG_NM = "test"
    DB_HOST = secret.DB_HOST
    DB_USER_NM = secret.DB_USER_NM
    DB_USER_PW = secret.DB_USER_PW
    DB_NAME = secret.DB_NAME

class ProductionConfig(Config):

    CONFIG_NM = "product"
    DB_HOST = secret.DB_HOST
    DB_USER_NM = secret.DB_USER_NM
    DB_USER_PW = secret.DB_USER_PW
    DB_NAME = secret.DB_NAME

class FactorySettings:
    @staticmethod
    def load():
        env_state = sys.argv[1]
        if env_state == 'local':
            return LocalConfig()
        elif env_state == 'product':
            return ProductionConfig()
        elif env_state == 'test':
            return TestConfig()

