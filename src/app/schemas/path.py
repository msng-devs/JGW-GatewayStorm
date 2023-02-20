from typing import Optional

from pydantic import BaseModel, Field


class PathAddRequest(BaseModel):
    path: str = Field(..., min_length=1, max_length=45)
    method_id: int
    role_id: Optional[int]
    service_id: int
    option: int

    class Config:
        orm_mode = True


class PathUpdateRequest(BaseModel):
    path: str = Field(..., min_length=1, max_length=45)
    method_id: int
    role_id: Optional[int]
    option: int

    class Config:
        orm_mode = True
