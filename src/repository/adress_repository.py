from fastapi import Depends
from src.schemas.request import CreateAdressRequest
from src.schemas.response import GetAdressResponse
from src.db.redis_storege import RedisClient


class AdressRepository:
    def __init__(
        self,
        redis_client: RedisClient = Depends()
    ):
        self._redis_client = redis_client

    async def create_address(self, data: CreateAdressRequest) -> bool:
        return await self._redis_client.set(data.phone, data.adress)

    async def get_address(self, phone: str) -> GetAdressResponse | None:
        adress = await self._redis_client.get(phone)
        if adress is None:
            return adress
        return GetAdressResponse(phone=phone, address=adress)
