from pydantic import BaseModel, ConfigDict
from datetime import datetime


class MessageCreate(BaseModel):
    content: str


class MessageRead(BaseModel):
    id: int
    chat_id: int
    content: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True, extra='ignore')