from fastapi import APIRouter, Request

ping_route = APIRouter()


@ping_route.get("/ping")
async def ping():

    return "PONG"
