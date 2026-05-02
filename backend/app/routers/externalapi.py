from fastapi import APIRouter, Depends
from app.repositories.externalapi_repo import StackOverflowRepo
from app.services.externalapi_service import ExternalService

router = APIRouter(prefix="/stack", tags=["StackExchange"])


def get_service() -> ExternalService:
    return ExternalService(StackOverflowRepo())


@router.get(
    "/respondidas",
    summary="Conteo de preguntas respondidas vs no respondidas"
)
async def get_respondidas(service: ExternalService = Depends(get_service)):
    return await service.respondidas_no_respondidas()


@router.get(
    "/mayor-reputacion",
    summary="Pregunta cuyo owner tiene la mayor reputacion"
)
async def get_top_reputacion(service: ExternalService = Depends(get_service)):
    return await service.mayor_reputacion()


@router.get(
    "/menor-vistas",
    summary="Pregunta con el menor numero de vistas"
)
async def get_menos_vistas(service: ExternalService = Depends(get_service)):
    return await service.menor_vistas()


@router.get(
    "/mas-vieja-y-actual",
    summary="Pregunta mas antigua y mas reciente del feed"
)
async def get_extremos_temporales(service: ExternalService = Depends(get_service)):
    return await service.mas_vieja_y_actual()