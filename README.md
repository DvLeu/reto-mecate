# Reto Técnico FullStack

Este es mi proyecto para el reto de 48 horas de Casa Mecate. Una app fullstack con backend en Python, frontend en React y base de datos PostgreSQL.

## Qué hace

- **Backend**: API REST con 8 endpoints. 4 para datos de vuelos en Mexico y 4 para datos de StackOverflow (tag Perl)
- **Frontend**: React que muestra los datos en una interfaz simple
- **Base de datos**: PostgreSQL con tablas de aeropuertos, aerolineas y vuelos

## Requisitos

Solo necesitas:

- Docker
- Docker Compose

## Pasos para correr

### 1. Clona o descarga el repo
Utilizando SSH 
```bash
git clone git@github.com:DvLeu/reto-mecate.git
cd reto-mecate
```

## Crea un archivo .env en la carpeta raiz del proyecto

```bash
cp .env.example .env
```

## El archivo .env debe tener esto :

```
# Base de datos
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin123
POSTGRES_DB=reto_db
POSTGRES_HOST=db
POSTGRES_PORT=5432

# URL para la DB 
DATABASE_URL=postgresql://admin:admin123@db:5432/reto_db

# API de StackExchange
STACK_API_URL=https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow
```

## Levantar los contenedores situandote en la raiz del proyecto

```bash
docker compose -up
```

El proceso tarda aproximadamente entre 40 segundos y 1 min por qué descarga las respectivas imagenes de Python y PostgreSQL

## Pasos para correr el Frontend

### Instala las dependencias 

```bash
cd frontend
npm install
npm run dev
```

### El frontend estará disponible en:

```txt
http://localhost:5173/
```

## URL's del proyecto

* **Frontend** : [http://localhost:5173](vscode-file://vscode-app/usr/share/code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)
* **Backend API** : [http://localhost:8000](vscode-file://vscode-app/usr/share/code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)
* **Docs automáticos del backend** : [http://localhost:8000/docs](vscode-file://vscode-app/usr/share/code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)

## Estructura del proyecto

```txt
reto-mecate/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── core/
│   │   │   └── config.py
│   │   ├── database.py
│   │   ├── seed.py
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── routers/
│   │   └── services/
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── api.js
│   │   └── main.jsx
│   ├── index.css
│   ├── package.json
│   └── vite.config.js
├── docker-compose.yml
├── .env.example
└── README.md
```

## Endpoints del backend

## API Endpoints

### Vuelos de México

- `GET http://localhost:8000/vuelos/aeropuerto-top`
- `GET http://localhost:8000/vuelos/aerolinea-top`
- `GET http://localhost:8000/vuelos/dia-top`
- `GET http://localhost:8000/vuelos/aerolineas-mas2`

### StackOverflow External API

- `GET http://localhost:8000/stackoverflow/respondidas`
- `GET http://localhost:8000/stackoverflow/mayor-reputacion`
- `GET http://localhost:8000/stackoverflow/menor-vistas`
- `GET http://localhost:8000/stackoverflow/extremos`

## Stack Tecnico de este reto

Todo fue basado en las versiones mas estables y listas para produccion.

Utilice PostgreSQL debido a que es una base de datos OpenSource muy utilizada en el mercado actualmente.

### Backend

* `fastapi==0.136.1`
* `uvicorn[standard]==0.32.0`
* `sqlalchemy==2.0.30`
* `psycopg2-binary==2.9.9`
* `httpx==0.27.0`
* `pydantic-settings==2.2.1`
* `python-dotenv==1.0.1`

### Frontend

* `react@19.2.5`
* `vite@8.0.10`
* `tailwindcss`

### Infraestructura

* Docker
* Docker Compose

## Notas del Proyecto

- **Sobre los IDs de los vuelos:** Para los vuelos, usé UUIDs en vez de los números duros que vienen en el readme del reto.
- Lo hice para que no sea tan fácil adivinar las URLs y que alguien empiece a probar `/vuelos/1`, `/vuelos/2`, etc. Me parece una adicion importante al proyecto como propuesta de mejora continua.
- Los datos de vuelos se crean solos la primera vez que corre el backend.
- Los datos de StackOverflow se bajan de internet cada vez que inicias la app.
- El archivo .env no lo subí a GitHub porque tiene las contraseñas. Por eso tienes que crearlo tú a partir del .env.example.
