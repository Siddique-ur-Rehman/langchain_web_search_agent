from sqlalchemy.orm import Session as DBSession
from database import engine, Session, Message


def create_session(session_id: str):
    with DBSession(engine) as db:
        session = Session(id=session_id)

        db.add(session)
        db.commit()


def save_message(session_id: str, role: str, content: str):
    with DBSession(engine) as db:
        message = Message(
            session_id=session_id,
            role=role,
            content=content
        )

        db.add(message)
        db.commit()


def get_messages(session_id: str):
    with DBSession(engine) as db:
        messages = (
            db.query(Message)
            .filter(Message.session_id == session_id)
            .order_by(Message.created_at)
            .all()
        )

        return [
            (message.role, message.content)
            for message in messages
        ]