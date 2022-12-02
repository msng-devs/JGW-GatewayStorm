from typing import Any

from sqlalchemy.orm import Session
from app.core.model import Method
from app.utlis.exceptions import NotFoundItemError


def findMethodAll(db: Session) -> Any | None:
    try:
        methods = db.query(Method).all()
        assert methods is not None
    except AssertionError:
        raise NotFoundItemError()
    except Exception as e:

        return None
    return methods
