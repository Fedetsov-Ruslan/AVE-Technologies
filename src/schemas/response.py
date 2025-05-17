from pydantic import BaseModel


class GetAdressResponse(BaseModel):
    phone: str
    address: str
