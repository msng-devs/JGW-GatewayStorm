import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.view.route import view_route
from app.api.route import api_route

app = FastAPI()
app.include_router(api_route)
app.include_router(view_route)
app.mount("/static", StaticFiles(directory="./resources/static"), name="static")

if __name__ == '__main__':
    uvicorn.run(app)

