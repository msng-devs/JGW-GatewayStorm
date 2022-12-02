from typing import Any

from sqlalchemy.orm import Session
from app.core.model import Role

from app.utlis.exceptions import NotFoundItemError


def findRoleAll(db: Session) -> Any | None:
    try:
        roles = db.query(Role).all()
        assert roles is not None
    except AssertionError:
        raise NotFoundItemError()
    except Exception as e:

        return None
    return roles
