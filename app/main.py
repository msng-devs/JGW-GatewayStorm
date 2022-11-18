from fastapi import FastAPI
import sys
from configs.config import FactorySettings
import api.routes

app = FastAPI()
Setting = FactorySettings.load()

if __name__ == '__main__':
    Setting = FactorySettings.load()

