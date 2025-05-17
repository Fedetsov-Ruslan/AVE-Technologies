from fastapi import Depends

from src.schemas.response import GetAdressResponse
from src.repository.adress_repository import AdressRepository


class AddressService:
    def __init__(
        self,
        address_repository: AdressRepository = Depends(),
    ):
        self.address_repository = address_repository

    async def create_address(self, data: dict) -> bool:
        return await self.address_repository.create_address(data)

    async def get_address(self, phone: str) -> GetAdressResponse | None:
        return await self.address_repository.get_address(phone=phone)
