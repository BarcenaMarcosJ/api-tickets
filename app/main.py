
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, status
from sqlmodel import Session

from app.database import crear_base_datos, obtener_sesion
from app.models import TicketActualizar, TicketCrear, TicketRespuesta
from app import services


@asynccontextmanager
async def lifespan(app: FastAPI):
    crear_base_datos()
    yield


app = FastAPI(
    title="API de Tickets - Atiendi",
    description="Servicio RESTful de gestión de tickets de Tecno Soluciones",
    version="1.0.0",
    lifespan=lifespan,
)


@app.post(
    "/tickets",
    response_model=TicketRespuesta,
    status_code=status.HTTP_201_CREATED,
)
def crear_ticket(
    datos: TicketCrear,
    session: Session = Depends(obtener_sesion),
):
    return services.crear_ticket(session, datos)


@app.get("/tickets", response_model=list[TicketRespuesta])
def listar_tickets(
    session: Session = Depends(obtener_sesion),
):
    return services.listar_tickets(session)


@app.get("/tickets/{id}", response_model=TicketRespuesta)
def consultar_ticket(
    id: int,
    session: Session = Depends(obtener_sesion),
):
    ticket = services.consultar_ticket(session, id)

    if ticket is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket no encontrado",
        )

    return ticket


@app.patch("/tickets/{id}", response_model=TicketRespuesta)
def actualizar_ticket(
    id: int,
    datos: TicketActualizar,
    session: Session = Depends(obtener_sesion),
):
    ticket = services.actualizar_ticket(session, id, datos)

    if ticket is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket no encontrado",
        )

    return ticket
