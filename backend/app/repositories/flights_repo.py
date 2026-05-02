from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models import Vuelo, Aerolinea, Aeropuerto


class FlightsRepository:
    def __init__(self, db: Session):
        self.db = db

    def aeropuerto_mayor_movimiento(self):
        return (
            self.db.query(
                Aeropuerto.nombre_aeropuerto,
                func.count(Vuelo.id).label("total")
            )
            .join(Vuelo, Vuelo.id_aeropuerto == Aeropuerto.id_aeropuerto)
            .group_by(Aeropuerto.nombre_aeropuerto)
            .order_by(func.count(Vuelo.id).desc())
            .first()
        )

    def aerolinea_mayor_vuelos(self):
        return (
            self.db.query(
                Aerolinea.nombre_aerolinea,
                func.count(Vuelo.id).label("total")
            )
            .join(Vuelo, Vuelo.id_aerolinea == Aerolinea.id_aerolinea)
            .group_by(Aerolinea.nombre_aerolinea)
            .order_by(func.count(Vuelo.id).desc())
            .first()
        )

    def dia_mayor_vuelos(self):
        return (
            self.db.query(
                Vuelo.dia,
                func.count(Vuelo.id).label("total")
            )
            .group_by(Vuelo.dia)
            .order_by(func.count(Vuelo.id).desc())
            .first()
        )

    def aerolineas_mas_2_vuelos_dia(self):
        return (
            self.db.query(
                Aerolinea.nombre_aerolinea,
                Vuelo.dia,
                func.count(Vuelo.id).label("total")
            )
            .join(Vuelo, Vuelo.id_aerolinea == Aerolinea.id_aerolinea)
            .group_by(Aerolinea.nombre_aerolinea, Vuelo.dia)
            .having(func.count(Vuelo.id) >= 2)
            .all()
        )