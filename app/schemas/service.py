from pydantic import BaseModel


class ServiceResponse(BaseModel):
    name : str
    index : str
    domain : str
    cnt : int

    class Config:
        orm_mode = True