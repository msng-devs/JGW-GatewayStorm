from typing import Any

from sqlalchemy.orm import Session
from app.core.model import Option

from app.utlis.exceptions import NotFoundItemError


def findOptionAll(db: Session) -> Any | None:
    try:
        options = db.query(Option).all()
        assert options is not None
    except AssertionError:
        raise NotFoundItemError()
    except Exception as e:

        return None
    return options
