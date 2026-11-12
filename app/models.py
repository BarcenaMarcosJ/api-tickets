
from datetime import datetime, timezone
from enum import Enum

from pydantic import field_validator
from sqlmodel import Field, SQLModel


class EstadoTicket(str, Enum):
    PENDIENTE = "pendiente"
    EN_ATENCION = "en_atencion"
    RESUELTO = "resuelto"
    CERRADO = "cerrado"


class DatosTicket(SQLModel):
    titulo: str
    descripcion: str

    @field_validator("titulo", "descripcion")
    @classmethod
    def validar_texto(cls, valor: str) -> str:
        valor = valor.strip()

        if not valor:
            raise ValueError("El campo no puede estar vacío")

        return valor


class Ticket(DatosTicket, table=True):
    id: int | None = Field(default=None, primary_key=True)
    estado: EstadoTicket = Field(default=EstadoTicket.PENDIENTE)
    fecha_creacion: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


class TicketCrear(DatosTicket):
    pass


class TicketActualizar(SQLModel):
    titulo: str | None = None
    descripcion: str | None = None
    estado: EstadoTicket | None = None

    @field_validator("titulo", "descripcion")
    @classmethod
    def validar_texto(cls, valor: str | None) -> str | None:
        if valor is not None:
            valor = valor.strip()

            if not valor:
                raise ValueError("El campo no puede estar vacío")

        return valor


class TicketRespuesta(SQLModel):
    id: int
    titulo: str
    descripcion: str
    estado: EstadoTicket
    fecha_creacion: datetime
