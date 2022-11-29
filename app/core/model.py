from app.core.db import Base
from sqlalchemy import Column, VARCHAR, INT, BLOB, TEXT, ForeignKey
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


class Service(Base):
    __tablename__ = 'SERVICE'
    __table_args__ = {'extend_existing': True}

    SERVICE_PK = Column(INT(), primary_key=True)
    SERVICE_NM = Column(VARCHAR(45), nullable=False, unique=True)
    SERVICE_DOMAIN = Column(VARCHAR(45), nullable=False, unique=True)
    SERVICE_INDEX = Column(TEXT(), nullable=True)

    def __repr__(self):
        return repr_create("Service", ["SERVICE_PK", "SERVICE_NM", "SERVICE_DOMAIN", "SERVICE_INDEX"]).format(self=self)


class Path(Base):
    __tablename__ = 'API_ROUTE'
    __table_args__ = {'extend_existing': True}

    API_ROUTE_PK = Column(INT(), primary_key=True)
    API_ROUTE_PATH = Column(VARCHAR(45), nullable=False)
    METHOD_METHOD_PK = Column(INT(),ForeignKey("METHOD.METHOD_PK"),nullable=False)
    ROLE_ROLE_PK = Column(INT(),ForeignKey("ROLE.ROLE_PK"),nullable=False)
    SERVICE_SERVICE_PK = Column(INT(),ForeignKey("SERVICE.SERVICE_PK"),nullable=False)

    API_ROUTE_GATEWAY_REFRESH = Column(BLOB(),nullable=True)
    API_ROUTE_ONLY_TOKEN = Column(BLOB(), nullable=True)
    API_ROUTE_OPTIONAL = Column(BLOB(), nullable=True)
    API_ROUTE_AUTHORIZATION = Column(BLOB(), nullable=True)

    method = relationship("Method")
    role = relationship("Role")
    service = relationship("Service")

    def __repr__(self):
        return repr_create("Path", ["API_ROUTE_PK","API_ROUTE_PATH","METHOD_METHOD_PK","ROLE_ROLE_PK","SERVICE_SERVICE_PK","API_ROUTE_GATEWAY_REFRESH","API_ROUTE_ONLY_TOKEN","API_ROUTE_OPTIONAL","API_ROUTE_AUTHORIZATION"]).format(self=self)
