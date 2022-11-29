import uvicorn
from fastapi import FastAPI
from app.configs.config import FactorySettings
from app.view.view import view_route

app = FastAPI()
app.include_router(view_route)
Setting = FactorySettings.load()

if __name__ == '__main__':
    Setting = FactorySettings.load()
    uvicorn.run(app)

