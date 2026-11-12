# API de Tickets - Atiendi

Servicio RESTful desarrollado como ejemplo de aplicación de los principios de la **Arquitectura Orientada a Servicios (SOA)** para la empresa ficticia Tecno Soluciones, dentro del Reto 5 de Arquitectura de Software de la UVEG.

## Objetivo

Implementar un servicio independiente y reutilizable para gestionar tickets de soporte relacionados con Atiendi. Sus operaciones se exponen mediante HTTP y JSON, permitiendo que diferentes aplicaciones puedan consumirlas sin acceder directamente a la lógica interna ni a la base de datos.

## Tecnologías utilizadas

- Python 3.12
- FastAPI
- SQLModel
- SQLite
- Uvicorn
- Docker

## Operaciones disponibles

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/tickets` | Registrar un ticket |
| GET | `/tickets` | Consultar todos los tickets |
| GET | `/tickets/{id}` | Consultar un ticket por identificador |
| PATCH | `/tickets/{id}` | Actualizar un ticket |

## Ejecución con Docker

**1. Clonar el repositorio y entrar al proyecto:**

```bash
git clone https://github.com/BarcenaMarcosJ/api-tickets.git
cd api-tickets
```

**2. Construir la imagen:**

```bash
sudo docker build -t atiendi-api:1.0 .
```

**3. Crear el directorio de almacenamiento y ejecutar el contenedor:**

```bash
mkdir -p data

sudo docker run -d \
  --name atiendi-api \
  -p 127.0.0.1:8000:8000 \
  -v "$PWD/data:/app/data" \
  atiendi-api:1.0
```

**4. Acceder a la documentación interactiva:**

http://localhost:8000/docs

La interfaz Swagger UI permite consultar las operaciones disponibles y realizar solicitudes de prueba.

## Relación con SOA

La implementación separa el contrato de datos (`models.py`), la persistencia (`database.py`), la lógica de gestión de tickets (`services.py`) y la interfaz RESTful (`main.py`).

Esta organización favorece la separación de responsabilidades y permite ofrecer la gestión de tickets como una capacidad reutilizable. Docker facilita su despliegue en un entorno reproducible.

**Nota:** Este proyecto es una demostración académica. No constituye una integración real con Atiendi ni incorpora autenticación o autorización de usuarios.
