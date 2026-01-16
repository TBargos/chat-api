from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Message
from app.schemas.message import MessageCreate


DEFAULT_LIMIT = 20
MAX_LIMIT = 100


def send_message(db: Session, message_in: MessageCreate) -> Message:
    message = Message(
        chat_id=message_in.chat_id,
        text=message_in.content,
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


def get_last_messages(db: Session, chat_id: int, limit: int = DEFAULT_LIMIT) -> list[Message]:
    """
    Получить последние N сообщений чата.
    Сообщения возвращаются в порядке от новых к старым.
    """
    limit = min(limit, MAX_LIMIT)

    stmt = (
        select(Message)
        .where(Message.chat_id == chat_id)
        .order_by(Message.created_at.desc())
        .limit(limit)
    )

    return db.execute(stmt).scalars().all()