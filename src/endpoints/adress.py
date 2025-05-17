from fastapi import APIRouter, Depends, Query

from src.schemas.request import CreateAdressRequest
from src.schemas.response import GetAdressResponse
from src.services.adress_service import AddressService


router = APIRouter(
    tags=["address"],
)


@router.post("/write-data")
async def create_address(
    data: CreateAdressRequest,
    adress_service: AddressService = Depends(),
) -> bool:
    """
    Создает новую запись или редактирует существующую
    
    :param data: Данные для записи
    :return: True, если запись создана или обновлена False в противном случае
    """
    return await adress_service.create_address(data)


@router.get("/check-data")
async def get_address(
    phone: str = Query(..., description="Номер телефона"),
    adress_service: AddressService = Depends(),
) -> GetAdressResponse | None:
    """
    Возвращает данные по номеру телефона
    
    :param phone: Нопер телефона
    :return: Данные GetAdressResponse
    """
    return await adress_service.get_address(phone=phone)
