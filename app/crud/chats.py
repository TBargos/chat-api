from sqlalchemy.orm import Session
from app.models import Chat
from app.schemas.chat import ChatCreate

from app.crud.messages import get_last_messages


def create_chat(db: Session, chat_in: ChatCreate) -> Chat:
    chat = Chat(title=chat_in.title)
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat


def get_chat(db: Session, chat_id: int, limit: int) -> Chat | None:
    chat = db.get(Chat, chat_id)
    if not chat:
        return None
    messages = get_last_messages(db, chat_id, limit)
    chat.messages = messages
    return chat


def delete_chat(db: Session, chat_id: int) -> bool:
    chat = db.get(Chat, chat_id)
    if not chat:
        return False
    db.delete(chat)
    db.commit()
    return True