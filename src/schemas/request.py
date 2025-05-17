from pydantic import BaseModel


class CreateAdressRequest(BaseModel):
    phone: str
    adress: str
