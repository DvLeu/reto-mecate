from app.repositories.flights_repo import FlightsRepository


class FlightsService:
    def __init__(self, repo: FlightsRepository):
        self.repo = repo

    def aeropuerto_mayor_movimiento(self):
        r = self.repo.aeropuerto_mayor_movimiento()
        return {"aeropuerto": r.nombre_aeropuerto, "total_movimientos": r.total}

    def aerolinea_mayor_vuelos(self):
        r = self.repo.aerolinea_mayor_vuelos()
        return {"aerolinea": r.nombre_aerolinea, "total_vuelos": r.total}

    def dia_mayor_vuelos(self):
        r = self.repo.dia_mayor_vuelos()
        return {"dia": str(r.dia), "total_vuelos": r.total}

    def aerolineas_mas_2_vuelos_dia(self):
        rows = self.repo.aerolineas_mas_2_vuelos_dia()
        return [
            {"aerolinea": r.nombre_aerolinea, "dia": str(r.dia), "vuelos": r.total}
            for r in rows
        ]