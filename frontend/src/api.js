const API_URL = "http://localhost:8000";

async function fetchJSON(path) {
  const res = await fetch(`${API_URL}${path}`);
  if (!res.ok) throw new Error(`Error ${res.status}`);
  return res.json();
}

export const api = {
  // Vuelos
  aeropuertoTop: () => fetchJSON("/vuelos/aeropuerto-mayor-movimiento"),
  aerolineaTop: () => fetchJSON("/vuelos/aerolinea-mayor-vuelos"),
  diaTop: () => fetchJSON("/vuelos/dia-mayor-vuelos"),
  aerolineasMas2: () => fetchJSON("/vuelos/aerolineas-mas-2-vuelos"),

  // StackExchange
  respondidas: () => fetchJSON("/stack/respondidas"),
  mayorReputacion: () => fetchJSON("/stack/mayor-reputacion"),
  menorVistas: () => fetchJSON("/stack/menor-vistas"),
  extremosTemporales: () => fetchJSON("/stack/mas-vieja-y-actual"),
};