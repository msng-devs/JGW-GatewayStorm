from fastapi import HTTPException
from starlette.responses import RedirectResponse
from app.utlis.exceptions import NotAuthenticatedException, NotValidUserIdOrPw


def NotAuthenticatedException_handler(request, exc):
    return RedirectResponse(url='/login')

def NotValidUserIdOrPw_handler(request, exc):
    return HTTPException(403)

def apply_exception_handlers(app):
    app.add_exception_handler(NotAuthenticatedException, NotAuthenticatedException_handler)
    app.add_exception_handler(NotValidUserIdOrPw, NotValidUserIdOrPw_handler)