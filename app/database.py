
from pathlib import Path

from sqlmodel import SQLModel, Session, create_engine

# Directorio donde se almacenará la base de datos
DIRECTORIO_DATOS = Path(__file__).resolve().parent.parent / "data"
DIRECTORIO_DATOS.mkdir(parents=True, exist_ok=True)

# Archivo SQLite
RUTA_BD = DIRECTORIO_DATOS / "tickets.db"

# Conexión a la base de datos
engine = create_engine(
    f"sqlite:///{RUTA_BD}",
    connect_args={"check_same_thread": False},
)


def crear_base_datos():
    # Importar el modelo para registrar la tabla
    from app.models import Ticket

    SQLModel.metadata.create_all(engine)


def obtener_sesion():
    with Session(engine) as session:
        yield session
