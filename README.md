# Globant Data Engineering API

## 📌 Descripción
Esta API ha sido desarrollada como parte del reto de ingeniería de datos de Globant. Utiliza **FastAPI** y **PostgreSQL** para gestionar la carga de archivos CSV y realizar consultas sobre los datos.

## 🚀 Características
- Recibe archivos CSV con datos históricos.
- Inserta los datos en una base de datos PostgreSQL.
- Permite inserción de transacciones en lotes (hasta 1000 registros por request).
- Endpoints para análisis de datos y consultas SQL.

## 🛠️ Instalación

### 1️⃣ Clonar el repositorio
```sh
git clone https://github.com/tu-usuario/globant-data-engineering.git
cd globant-data-engineering
```

### 2️⃣ Crear y activar el entorno virtual
```sh
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3️⃣ Instalar dependencias
```sh
pip install -r requirements.txt
```

### 4️⃣ Configurar PostgreSQL
Crea la base de datos y el usuario:
```sql
CREATE DATABASE dbname;
CREATE USER user WITH PASSWORD 'password';
ALTER ROLE user SET client_encoding TO 'utf8';
ALTER ROLE user SET default_transaction_isolation TO 'read committed';
ALTER ROLE user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE dbname TO user;
```

### 5️⃣ Ejecutar la API
```sh
uvicorn app:app --reload
```

📌 Accede a la documentación de la API en [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs).

## 🗂️ Endpoints
### 📂 Subida de archivos CSV
**POST `/upload-csv/`**
Carga archivos CSV de departamentos, trabajos y empleados contratados.

### 📊 Consultas de datos
- **GET `/hired-employees-by-quarter/`** → Cantidad de empleados contratados por trimestre en 2021.
- **GET `/departments-above-average-hiring/`** → Departamentos que contrataron más empleados que el promedio.

## 🐳 Dockerización
Puedes ejecutar la API en un contenedor Docker:
```sh
docker-compose up -d
```

## ✨ Autor
Desarrollado por **Eduardo Gowland** para el desafío de ingeniería de datos de Globant.

