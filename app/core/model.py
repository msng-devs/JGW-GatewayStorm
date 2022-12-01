from typing import Optional

from app.core.db import Base
from sqlalchemy import Column, VARCHAR, INT, BLOB, TEXT, ForeignKey, Boolean
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

    SERVICE_PK = Column(INT(), primary_key=True, autoincrement=True)
    SERVICE_NM = Column(VARCHAR(45), nullable=False, unique=True)
    SERVICE_DOMAIN = Column(VARCHAR(45), nullable=False, unique=True)
    SERVICE_INDEX = Column(TEXT(), nullable=True)

    def __repr__(self):
        return repr_create("Service", ["SERVICE_PK", "SERVICE_NM", "SERVICE_DOMAIN", "SERVICE_INDEX"]).format(self=self)

    def __init__(self, **entries):
        self.__dict__.serviceUpdate(entries)

class Path(Base):
    __tablename__ = 'API_ROUTE'
    __table_args__ = {'extend_existing': True}

    API_ROUTE_PK = Column(INT(), primary_key=True, autoincrement=True)
    API_ROUTE_PATH = Column(VARCHAR(45), nullable=False)
    METHOD_METHOD_PK = Column(INT(),ForeignKey("METHOD.METHOD_PK"),nullable=False)
    ROLE_ROLE_PK = Column(INT(),ForeignKey("ROLE.ROLE_PK"),nullable=False)
    SERVICE_SERVICE_PK = Column(INT(),ForeignKey("SERVICE.SERVICE_PK"),nullable=False)

    API_ROUTE_GATEWAY_REFRESH = Column(Boolean(),nullable=True)
    API_ROUTE_ONLY_TOKEN = Column(Boolean(), nullable=True)
    API_ROUTE_OPTIONAL = Column(Boolean(), nullable=True)
    API_ROUTE_AUTHORIZATION = Column(Boolean(), nullable=True)

    method = relationship("Method")
    role = relationship("Role")
    service = relationship("Service", lazy="joined")

    def __repr__(self):
        return repr_create("Path", ["API_ROUTE_PK","API_ROUTE_PATH","METHOD_METHOD_PK","ROLE_ROLE_PK","SERVICE_SERVICE_PK","API_ROUTE_GATEWAY_REFRESH","API_ROUTE_ONLY_TOKEN","API_ROUTE_OPTIONAL","API_ROUTE_AUTHORIZATION"]).format(self=self)

    def __init__(self, **entries):
        self.__dict__.update(entries)

    def get_option(self) -> str:

        if self.API_ROUTE_ONLY_TOKEN == False and self.API_ROUTE_OPTIONAL == False and self.API_ROUTE_AUTHORIZATION == False and self.ROLE_ROLE_PK == None:
            return "NO_AUTH"

        elif self.API_ROUTE_ONLY_TOKEN == False and self.API_ROUTE_OPTIONAL == False and self.API_ROUTE_AUTHORIZATION == True and self.ROLE_ROLE_PK == None:
            return "AUTH"

        elif self.API_ROUTE_ONLY_TOKEN == True and self.API_ROUTE_OPTIONAL == False and self.API_ROUTE_AUTHORIZATION == True and self.ROLE_ROLE_PK == None:
            return "ONLY_TOKEN_AUTH"

        elif self.API_ROUTE_ONLY_TOKEN == False and self.API_ROUTE_OPTIONAL == False and self.API_ROUTE_AUTHORIZATION == True and self.ROLE_ROLE_PK != None:
            return "RBAC"

        elif self.API_ROUTE_ONLY_TOKEN == False and self.API_ROUTE_OPTIONAL == True and self.API_ROUTE_AUTHORIZATION == True and self.ROLE_ROLE_PK == None:
            return "AUTH_OPTIONAL"

    def set_option(self,option:str,role_id : Optional[int]) -> None:
        if option == "NO_AUTH":
            self.API_ROUTE_ONLY_TOKEN = self.API_ROUTE_OPTIONAL = self.API_ROUTE_AUTHORIZATION = False
            self.ROLE_ROLE_PK = None

        elif option == "AUTH":
            self.API_ROUTE_ONLY_TOKEN = self.API_ROUTE_OPTIONAL = False
            self.API_ROUTE_AUTHORIZATION = True
            self.ROLE_ROLE_PK = None

        elif option == "ONLY_TOKEN_AUTH":
            self.API_ROUTE_OPTIONAL = False
            self.API_ROUTE_AUTHORIZATION = self.API_ROUTE_ONLY_TOKEN = True
            self.ROLE_ROLE_PK = None

        elif option == "RBAC":
            self.API_ROUTE_OPTIONAL = self.API_ROUTE_ONLY_TOKEN = False
            self.API_ROUTE_AUTHORIZATION = True
            self.ROLE_ROLE_PK = role_id

        elif option == "AUTH_OPTIONAL":
            self.API_ROUTE_ONLY_TOKEN = False
            self.API_ROUTE_AUTHORIZATION = self.API_ROUTE_OPTIONAL = True
            self.ROLE_ROLE_PK = None