import { useEffect, useState } from "react";
import { api } from "./api";

function Card({ title, children, loading }) {
  return (
    <div className="bg-white border border-gray-200 rounded">
      <div className="bg-black text-white p-3 rounded-t">
        <h3 className="text-sm font-bold uppercase">{title}</h3>
      </div>
      <div className="p-4">
        {loading ? <div className="text-gray-400">Cargando...</div> : children}
      </div>
    </div>
  );
}

function Section({ title, subtitle, children }) {
  return (
    <section className="mb-10">
      <h2 className="text-2xl font-bold text-black mb-1">{title}</h2>
      <p className="text-gray-600 mb-4 text-sm">{subtitle}</p>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">{children}</div>
    </section>
  );
}

export default function App() {
  const [data, setData] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    console.log("Cargando datos del backend...");

    Promise.all([
      api.aeropuertoTop(),
      api.aerolineaTop(),
      api.diaTop(),
      api.aerolineasMas2(),
      api.respondidas(),
      api.mayorReputacion(),
      api.menorVistas(),
      api.extremosTemporales(),
    ])
      .then(
        ([
          aeropuerto,
          aerolinea,
          dia,
          aerolineasMas2,
          respondidas,
          mayorRep,
          menorVistas,
          extremos,
        ]) => {
          console.log("Aeropuerto:", aeropuerto);
          console.log("Aerolinea:", aerolinea);
          console.log("Mayor reputacion:", mayorRep);
          console.log("Menor vistas:", menorVistas);

          setData({
            aeropuerto,
            aerolinea,
            dia,
            aerolineasMas2,
            respondidas,
            mayorRep,
            menorVistas,
            extremos,
          });
          setLoading(false);
        },
      )
      .catch((err) => {
        console.error("Error:", err);
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center p-4 bg-white">
        <div className="bg-red-100 border-2 border-red-400 text-red-700 p-4 rounded">
          Error: {error}
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-white">
      <header className="bg-black text-white p-6">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-3xl font-bold">Reto Técnico FullStack</h1>
        </div>
      </header>

      <main className="w-full mx-auto p-4 md:p-6">
        <Section
          title="Análisis de Vuelos"
          subtitle="Datos sobre vuelos, aeropuertos y aerolíneas en México."
        >
          <Card
            title="Aeropuerto con Más Movimiento"
            loading={loading}
          >
            {data.aeropuerto && (
              <div>
                <p className="text-2xl font-bold text-black">
                  {data.aeropuerto.aeropuerto}
                </p>
                <p className="text-xs text-gray-600 mt-1">
                  {data.aeropuerto.total_movimientos} movimientos
                </p>
              </div>
            )}
          </Card>

          <Card title="Aerolínea con Más Vuelos" loading={loading}>
            {data.aerolinea && (
              <div>
                <p className="text-2xl font-bold text-black">
                  {data.aerolinea.aerolinea}
                </p>
                <p className="text-xs text-gray-600 mt-1">
                  {data.aerolinea.total_vuelos} vuelos
                </p>
              </div>
            )}
          </Card>

          <Card
            title="Día con Mayor Tráfico Aéreo"
            loading={loading}
          >
            {data.dia && (
              <div>
                <p className="text-2xl font-bold text-black">
                  {data.dia.dia}
                </p>
                <p className="text-xs text-gray-600 mt-1">
                  {data.dia.total_vuelos} vuelos
                </p>
              </div>
            )}
          </Card>

          <Card
            title="Aerolíneas con >2 Vuelos en un Día"
            loading={loading}
          >
            {data.aerolineasMas2 && (
              <div>
                {data.aerolineasMas2.length > 0 ? (
                  data.aerolineasMas2.map((a, i) => (
                    <div key={i} className="mb-2 pb-2 border-b border-gray-200 last:border-0">
                      <p className="font-bold text-black text-sm">{a.aerolinea}</p>
                      <p className="text-xs text-gray-600">
                        {a.dia} - {a.vuelos} vuelos
                      </p>
                    </div>
                  ))
                ) : (
                  <p className="text-sm text-gray-500">No hay datos que cumplan la condición.</p>
                )}
              </div>
            )}
          </Card>
        </Section>

        <Section
          title="StackOverflow Tag : Perl"
          subtitle="Estadísticas de preguntas con la etiqueta perl en StackOverflow."
        >
          <Card
            title="Estado de las Preguntas"
            loading={loading}
          >
            {data.respondidas && (
              <div>
                <div className="mb-3">
                  <p className="text-2xl font-bold text-green-600">
                    {data.respondidas.respondidas}
                  </p>
                  <p className="text-xs text-gray-600">respondidas</p>
                </div>
                <div className="mb-3">
                  <p className="text-2xl font-bold text-red-600">
                    {data.respondidas.no_respondidas}
                  </p>
                  <p className="text-xs text-gray-600">sin responder</p>
                </div>
                <p className="text-xs text-gray-600">
                  Total: {data.respondidas.total}
                </p>
              </div>
            )}
          </Card>

          <Card
            title="Pregunta con Mejor Reputación"
            loading={loading}
          >
            {data.mayorRep && (
              <div>
                <a
                  href={data.mayorRep.link}
                  target="_blank"
                  rel="noreferrer"
                  className="text-blue-600 underline text-xs hover:text-blue-800"
                >
                  {data.mayorRep.titulo}
                </a>
                <p className="text-xs text-gray-600 mt-2">
                  {data.mayorRep.owner}
                </p>
                <p className="text-lg font-bold text-black mt-1">
                  {data.mayorRep.reputacion.toLocaleString()}
                </p>
              </div>
            )}
          </Card>

          <Card title="La Pregunta Menos Popular" loading={loading}>
            {data.menorVistas && (
              <div>
                <a
                  href={data.menorVistas.link}
                  target="_blank"
                  rel="noreferrer"
                  className="text-blue-600 underline text-xs hover:text-blue-800"
                >
                  {data.menorVistas.titulo}
                </a>
                <p className="text-lg font-bold text-black mt-2">
                  {data.menorVistas.vistas} vistas
                </p>
              </div>
            )}
          </Card>

          <Card title="Extremos Temporales" loading={loading}>
            {data.extremos && (
              <div>
                <div className="mb-3">
                  <p className="text-xs text-gray-600 font-bold mb-1">
                    MÁS ANTIGUA
                  </p>
                  <a
                    href={data.extremos.mas_vieja.link}
                    target="_blank"
                    rel="noreferrer"
                    className="text-blue-600 underline text-xs hover:text-blue-800"
                  >
                    {data.extremos.mas_vieja.titulo}
                  </a>
                </div>
                <div>
                  <p className="text-xs text-gray-600 font-bold mb-1">
                    MÁS RECIENTE
                  </p>
                  <a
                    href={data.extremos.mas_actual.link}
                    target="_blank"
                    rel="noreferrer"
                    className="text-blue-600 underline text-xs hover:text-blue-800"
                  >
                    {data.extremos.mas_actual.titulo}
                  </a>
                </div>
              </div>
            )}
          </Card>
        </Section>

        <footer className="text-center text-xs text-gray-500 border-t border-gray-300 pt-4">
          Reto tecnico - Casa Mecate
        </footer>
      </main>
    </div>
  );
}
