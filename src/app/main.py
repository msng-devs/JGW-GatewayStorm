from app.configs.config import settings
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from app.view.route import view_route
from app.api.route import api_route
from app.utlis.exception_handler import apply_exception_handlers

app = FastAPI()
app.include_router(api_route)
app.include_router(view_route)
app.mount("/static", StaticFiles(directory="app/resources/static"), name="static")
apply_exception_handlers(app)

origins = [
    "http://127.0.0.1:8000/",
    "http://localhost:8000"
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print(f"welcome! init ID: {settings.USER_ID} init PW: {settings.USER_PW}")
if __name__ == '__main__':

    uvicorn.run(app)
