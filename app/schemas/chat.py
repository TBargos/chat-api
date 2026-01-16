from pydantic import BaseModel, ConfigDict
from datetime import datetime

from .message import MessageRead


class ChatCreate(BaseModel):
    title: str


class ChatRead(BaseModel):
    id: int
    title: str
    created_at: datetime
    messages: list[MessageRead]

    model_config = ConfigDict(from_attributes=True, extra='ignore')
