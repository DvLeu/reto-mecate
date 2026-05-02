from datetime import date
from sqlalchemy.orm import Session
from app.models import Aerolinea, Aeropuerto, Movimiento, Vuelo


def seed_database(db: Session) -> None:
    if db.query(Aerolinea).count() > 0:
        return

    aerolineas = [
        Aerolinea(id_aerolinea=1, nombre_aerolinea="Volaris"),
        Aerolinea(id_aerolinea=2, nombre_aerolinea="Aeromar"),
        Aerolinea(id_aerolinea=3, nombre_aerolinea="Interjet"),
        Aerolinea(id_aerolinea=4, nombre_aerolinea="Aeromexico"),
    ]

    aeropuertos = [
        Aeropuerto(id_aeropuerto=1, nombre_aeropuerto="Benito Juarez"),
        Aeropuerto(id_aeropuerto=2, nombre_aeropuerto="Guanajuato"),
        Aeropuerto(id_aeropuerto=3, nombre_aeropuerto="La Paz"),
        Aeropuerto(id_aeropuerto=4, nombre_aeropuerto="Oaxaca"),
    ]

    movimientos = [
        Movimiento(id_movimiento=1, descripcion="Salida"),
        Movimiento(id_movimiento=2, descripcion="Llegada"),
    ]

    vuelos = [
        Vuelo(id_aerolinea=1, id_aeropuerto=1, id_movimiento=1, dia=date(2021, 5, 2)),
        Vuelo(id_aerolinea=2, id_aeropuerto=1, id_movimiento=1, dia=date(2021, 5, 2)),
        Vuelo(id_aerolinea=3, id_aeropuerto=2, id_movimiento=2, dia=date(2021, 5, 2)),
        Vuelo(id_aerolinea=4, id_aeropuerto=3, id_movimiento=2, dia=date(2021, 5, 2)),
        Vuelo(id_aerolinea=1, id_aeropuerto=3, id_movimiento=2, dia=date(2021, 5, 2)),
        Vuelo(id_aerolinea=2, id_aeropuerto=1, id_movimiento=1, dia=date(2021, 5, 2)),
        Vuelo(id_aerolinea=2, id_aeropuerto=3, id_movimiento=1, dia=date(2021, 5, 4)),
        Vuelo(id_aerolinea=3, id_aeropuerto=4, id_movimiento=1, dia=date(2021, 5, 4)),
        Vuelo(id_aerolinea=3, id_aeropuerto=4, id_movimiento=1, dia=date(2021, 5, 4)),
    ]

    db.add_all(aerolineas + aeropuertos + movimientos + vuelos)
    db.commit()
    print(f"Base de datos populada correctamente")