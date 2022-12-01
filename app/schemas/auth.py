from pydantic import BaseModel

class LoginReqeust(BaseModel):
    id:str
    pw:str

