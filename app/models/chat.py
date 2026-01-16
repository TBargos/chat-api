from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Mapped, relationship

from app.database import Base


class Chat(Base):
    __tablename__ = "chats"

    id: Mapped[int] = Column(
        Integer,
        primary_key=True,
    )

    title: Mapped[str] = Column(
        String,
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

    # Связь: один чат → много сообщений
    messages: Mapped[list["Message"]] = relationship(
        "Message",
        back_populates="chat",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<Chat id={self.id} title={self.title!r}>"
