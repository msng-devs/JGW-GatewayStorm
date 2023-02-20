from typing import Optional

from app.core.db import Base
from sqlalchemy import Column, VARCHAR, INT, TEXT, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.utlis.repr import repr_create


class Method(Base):
    __tablename__ = 'METHOD'
    __table_args__ = {'extend_existing': True}

    METHOD_PK = Column(INT(), primary_key=True)
    METHOD_NM = Column(VARCHAR(45), nullable=False, unique=True)

    def __repr__(self):
        return repr_create("Method", ["METHOD_PK", "METHOD_NM"]).format(self=self)


class Role(Base):
    __tablename__ = 'ROLE'
    __table_args__ = {'extend_existing': True}

    ROLE_PK = Column(INT(), primary_key=True)
    ROLE_NM = Column(VARCHAR(45), nullable=False, unique=True)

    def __repr__(self):
        return repr_create("Role", ["ROLE_PK", "ROLE_NM"]).format(self=self)


class Option(Base):
    __tablename__ = 'ROUTE_OPTION'
    __table_args__ = {'extend_existing': True}

    ROUTE_OPTION_PK = Column(INT(), primary_key=True)
    ROUTE_OPTION_NM = Column(VARCHAR(50), nullable=False, unique=True)

    def __repr__(self):
        return repr_create("Option", ["ROUTE_OPTION_PK", "ROUTE_OPTION_NM"]).format(self=self)


class Service(Base):
    __tablename__ = 'SERVICE'
    __table_args__ = {'extend_existing': True}

    SERVICE_PK = Column(INT(), primary_key=True, autoincrement=True)
    SERVICE_NM = Column(VARCHAR(45), nullable=False, unique=True)
    SERVICE_DOMAIN = Column(VARCHAR(45), nullable=False, unique=True)
    SERVICE_INDEX = Column(TEXT(), nullable=True)

    def __repr__(self):
        return repr_create("Service", ["SERVICE_PK", "SERVICE_NM", "SERVICE_DOMAIN", "SERVICE_INDEX"]).format(self=self)

    def __init__(self, **entries):
        self.__dict__.update(entries)


class Path(Base):
    __tablename__ = 'API_ROUTE'
    __table_args__ = {'extend_existing': True}

    API_ROUTE_PK = Column(INT(), primary_key=True, autoincrement=True)
    API_ROUTE_PATH = Column(VARCHAR(45), nullable=False)
    METHOD_METHOD_PK = Column(INT(), ForeignKey("METHOD.METHOD_PK"), nullable=False)
    ROLE_ROLE_PK = Column(INT(), ForeignKey("ROLE.ROLE_PK"), nullable=True)
    SERVICE_SERVICE_PK = Column(INT(), ForeignKey("SERVICE.SERVICE_PK"), nullable=False)
    ROUTE_OPTION_ROUTE_OPTION_PK = Column(INT(), ForeignKey("ROUTE_OPTION.ROUTE_OPTION_PK"), nullable=False)

    method = relationship("Method")
    role = relationship("Role")
    option = relationship("Option")
    service = relationship("Service", lazy="joined")

    def __repr__(self):
        return repr_create("Path",
                           ["API_ROUTE_PK", "API_ROUTE_PATH", "METHOD_METHOD_PK", "ROLE_ROLE_PK", "SERVICE_SERVICE_PK",
                            "ROUTE_OPTION_ROUTE_OPTION_PK"]).format(self=self)

    def __init__(self, **entries):
        self.__dict__.update(entries)
