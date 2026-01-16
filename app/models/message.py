from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from app.database import Base


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = Column(
        Integer,
        primary_key=True,
    )

    chat_id: Mapped[int] = Column(
        Integer,
        ForeignKey("chats.id", ondelete="CASCADE"),
        nullable=False,
    )

    text: Mapped[str] = Column(
        String,
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

    # Связь: много сообщений → один чат
    chat: Mapped["Chat"] = relationship(
        "Chat",
        back_populates="messages",
    )

    def __repr__(self) -> str:
        return f"<Message id={self.id} chat_id={self.chat_id}>"
