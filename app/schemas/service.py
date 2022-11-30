from pydantic import BaseModel, Field


class ServiceAddRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=45)
    index: str = Field(..., max_length=256)
    domain: str = Field(...,min_length=1, max_length=45)

    class Config:
        orm_mode = True


class ServiceUpdateRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=45)
    index: str = Field(..., max_length=256)
    domain: str = Field(...,min_length=1, max_length=45)

    class Config:
        orm_mode = True
