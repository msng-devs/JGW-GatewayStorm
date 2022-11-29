from app.utlis.logger import logger

class NotFoundItemError(Exception):
    logger.debug("raise NotFoundItemError!",Exception.__traceback__)