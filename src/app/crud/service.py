import logging
from typing import Any

from sqlalchemy.orm import Session
from app.core.model import Service
from app.utlis.exceptions import NotFoundItemError


def findServiceAll(db: Session) -> Any | list:
    try:
        services = db.query(Service).all()
        assert services is not None
    except AssertionError:
        raise NotFoundItemError()

    except Exception as e:
        logging.info(e)
        return None

    return services


def serviceAdd(db: Session, new_service: Service):
    try:
        db.add(new_service)

    except Exception as e:
        return None

    db.commit()

def findById(db: Session, target_id: int):
    try:
        target_service = db.query(Service).filter(Service.SERVICE_PK == target_id).one()
        assert target_service is not None

    except AssertionError:
        raise NotFoundItemError()
    except Exception as e:

        return None

    return target_service

def serviceUpdate(db: Session, target_id: int, new_service: Service):
    try:
        target_service = db.query(Service).filter(Service.SERVICE_PK == target_id).one()
        assert target_service is not None
        target_service.SERVICE_NM = new_service.SERVICE_NM
        target_service.SERVICE_DOMAIN = new_service.SERVICE_DOMAIN
        target_service.SERVICE_INDEX = new_service.SERVICE_INDEX

    except AssertionError:
        raise NotFoundItemError()
    except Exception as e:

        return None

    db.commit()


def serviceDelete(db: Session, target_id: int):
    try:
        db.query(Service).filter(Service.SERVICE_PK == target_id).delete()

    except Exception as e:

        return None

    db.commit()
