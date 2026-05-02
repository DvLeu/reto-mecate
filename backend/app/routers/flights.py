from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repositories.flights_repo import FlightsRepository
from app.services.flights_service import FlightsService

router = APIRouter(prefix="/vuelos", tags=["Vuelos"])


def get_service(db: Session = Depends(get_db)) -> FlightsService:
    return FlightsService(FlightsRepository(db))


@router.get(
    "/aeropuerto-mayor-movimiento",
    summary="Aeropuerto con mas movimiento durante el periodo"
)
def get_top_aeropuerto(service: FlightsService = Depends(get_service)):
    return service.aeropuerto_mayor_movimiento()


@router.get(
    "/aerolinea-mayor-vuelos",
    summary="Aerolinea con mayor cantidad de vuelos"
)
def get_top_aerolinea(service: FlightsService = Depends(get_service)):
    return service.aerolinea_mayor_vuelos()


@router.get(
    "/dia-mayor-vuelos",
    summary="Dia con mayor concentracion de vuelos"
)
def get_dia_pico(service: FlightsService = Depends(get_service)):
    return service.dia_mayor_vuelos()


@router.get(
    "/aerolineas-mas-2-vuelos",
    summary="Aerolineas que superaron 2 vuelos en un mismo dia"
)
def get_aerolineas_alta_frecuencia(service: FlightsService = Depends(get_service)):
    return service.aerolineas_mas_2_vuelos_dia()