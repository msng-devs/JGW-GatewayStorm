import logging

from fastapi import HTTPException
from fastapi_csrf_protect.exceptions import TokenValidationError, InvalidHeaderError
from starlette import status
from starlette.responses import RedirectResponse, JSONResponse

from app.utlis.logger import logger
from app.utlis.exceptions import NotAuthenticatedException, NotFoundItemError


def NotAuthenticatedException_handler(request, exc):
    logging.info("인증 실패")
    return RedirectResponse(url='/login')

def NotFoundItemErrorException_handler(request, exc):

    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={'detail': '해당 데이터를 찾을 수 없습니다!'}
    )


def TokenValidationErrorException_handler(request, exc):

    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={'detail': 'CSRF 토큰 인증에 실패했습니다.'}
    )

def apply_exception_handlers(app):
    app.add_exception_handler(NotAuthenticatedException, NotAuthenticatedException_handler)
    app.add_exception_handler(TokenValidationError,TokenValidationErrorException_handler)
    app.add_exception_handler(InvalidHeaderError,TokenValidationErrorException_handler)
    app.add_exception_handler(NotFoundItemError,NotFoundItemErrorException_handler)