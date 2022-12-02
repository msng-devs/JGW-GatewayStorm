from fastapi import HTTPException
from starlette.responses import RedirectResponse
from app.utlis.exceptions import NotAuthenticatedException


def NotAuthenticatedException_handler(request, exc):
    return RedirectResponse(url='/login')



def apply_exception_handlers(app):
    app.add_exception_handler(NotAuthenticatedException, NotAuthenticatedException_handler)
