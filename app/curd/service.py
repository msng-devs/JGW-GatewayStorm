from typing import Any

from sqlalchemy.orm import Session
from app.core.model import Service
from app.utlis.logger import logger
from app.utlis.exceptions import NotFoundItemError


def findAll(db: Session) -> Any | None:
    try:
        services = db.query(Service).all()
        assert services is not None
    except AssertionError:
        raise NotFoundItemError()

    except Exception as e:
        logger.error(e.__traceback__)
        return None

    return services


def add(db: Session, new_service: Service):
    try:
        db.add(new_service)

    except Exception as e:
        logger.error(e.__traceback__)
        return None

    db.commit()


def update(db: Session, target_id: int, new_service: Service):
    try:
        target_service = db.query(Service).filter(Service.SERVICE_PK == target_id).one()
        assert target_service is not None
        target_service.SERVICE_NM = new_service.SERVICE_NM
        target_service.SERVICE_DOMAIN = new_service.SERVICE_DOMAIN
        target_service.SERVICE_INDEX = new_service.SERVICE_INDEX

    except AssertionError:
        raise NotFoundItemError()
    except Exception as e:
        logger.error(e.__traceback__)
        return None

    db.commit()


def delete(db: Session, target_id: int):
    try:
        db.query(Service).filter(Service.SERVICE_PK == target_id).delete()

    except Exception as e:
        logger.error(e.__traceback__)
        return None

    db.commit()
