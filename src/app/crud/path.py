from typing import Any, List

from sqlalchemy.orm import Session
from src.app.core.model import Path
from src.app.utlis.exceptions import NotFoundItemError


def findPathAllByServiceID(db: Session, service_id: int) -> Any | None:
    try:
        paths = db.query(Path).where(Path.SERVICE_SERVICE_PK == service_id).order_by(Path.API_ROUTE_PATH).order_by(
            Path.METHOD_METHOD_PK).all()
        assert paths is not None
    except AssertionError:
        raise NotFoundItemError()
    except Exception as e:

        return None
    return paths


def findOptionAll() -> List[str]:
    return ["NO_AUTH", "AUTH", "ONLY_TOKEN_AUTH", "RBAC", "AUTH_OPTIONAL"]


def pathAdd(db: Session, new_path: Path):
    try:
        db.add(new_path)

    except Exception as e:

        return None

    db.commit()


def pathUpdate(db: Session, target_id: int, new_path: Path):
    try:
        target_path = db.query(Path).filter(Path.API_ROUTE_PK == target_id).one()
        assert target_path is not None
        target_path.API_ROUTE_PATH = new_path.API_ROUTE_PATH
        target_path.METHOD_METHOD_PK = new_path.METHOD_METHOD_PK

        target_path.API_ROUTE_OPTIONAL = new_path.API_ROUTE_OPTIONAL
        target_path.API_ROUTE_ONLY_TOKEN = new_path.API_ROUTE_ONLY_TOKEN
        target_path.API_ROUTE_AUTHORIZATION = new_path.API_ROUTE_AUTHORIZATION
        target_path.ROLE_ROLE_PK = new_path.ROLE_ROLE_PK

    except AssertionError:
        raise NotFoundItemError()
    except Exception as e:

        return None

    db.commit()


def pathDelete(db: Session, target_id: int):
    try:
        db.query(Path).filter(Path.API_ROUTE_PK == target_id).serviceDelete()

    except Exception as e:

        return None

    db.commit()
