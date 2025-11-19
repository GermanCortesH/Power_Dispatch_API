# Distribuidor de energia (Powerplant Dispatcher).

Este proyecto implementa un servicio REST simple usando FastAPI para calcular el plan de producción óptimo de un conjunto de centrales eléctricas, siguiendo la lógica de Orden de Mérito, el cual se entiende como: la planta con un coste de generación mas económico será 
utilizada primero para suplir la demanda.

---
## Cómo Empezar
### 1. Requisitos

Necesitas tener instalados en tu máquina:

* **Docker Desktop** (para construir y ejecutar el contenedor).
* **Python 3.11+** (para desarrollo local, ver el código y demás, aunque Docker se encarga de inicializar el proyecto).

### 2. Estructura del Proyecto

La estructura principal del repositorio es la siguiente:

* **`Raíz_del_proyecto/`** 
    * `app/` (Módulo principal)
        * `main.py`: Lógica del endpoint y la Orden de Mérito.
        * `models.py`: Modelos de datos (Pydantic).
    * `Dockerfile`: Instrucciones para construir la imagen de Docker.
    * `docker-compose.yml`: Definición del servicio de Docker.
    * `README.md`: Documentación del proyecto.

## Construcción y Lanzamiento de la API

El servicio se despliega usando Docker Compose, que se encarga de crear el ambiente necesario y ejecutar la aplicación.

### A. Construir y Lanzar la API

Ejecuta el siguiente comando desde la carpeta raíz:
* `docker compose up --build -d`
* Abre el siguiente link en algún buscador `http://localhost:8888/docs`
* agrega cambios en los datos de entrada y ejecuta la consulta de la api para ver la salida
