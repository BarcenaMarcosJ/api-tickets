
from sqlmodel import Session, select

from app.models import Ticket, TicketCrear, TicketActualizar


def crear_ticket(session: Session, datos: TicketCrear) -> Ticket:
    ticket = Ticket.model_validate(datos)

    session.add(ticket)
    session.commit()
    session.refresh(ticket)

    return ticket


def listar_tickets(session: Session) -> list[Ticket]:
    consulta = select(Ticket)
    return list(session.exec(consulta).all())


def consultar_ticket(session: Session, ticket_id: int) -> Ticket | None:
    return session.get(Ticket, ticket_id)


def actualizar_ticket(
    session: Session,
    ticket_id: int,
    datos: TicketActualizar
) -> Ticket | None:

    ticket = session.get(Ticket, ticket_id)

    if ticket is None:
        return None

    cambios = datos.model_dump(exclude_unset=True)

    ticket.sqlmodel_update(cambios)

    session.add(ticket)
    session.commit()
    session.refresh(ticket)

    return ticket
