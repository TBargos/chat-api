from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from app.database import get_session
from app.schemas.message import MessageCreate, MessageRead
from app.crud import messages as message_crud

router = APIRouter(
    prefix="/chats/{chat_id}/messages",
    tags=["messages"],
)


@router.post("/", response_model=MessageRead, status_code=201)
def create_message(chat_id: int, data: MessageCreate, session: Session = Depends(get_session)):
    try:
        message = message_crud.send_message(
            db=session,
            message_in=data,
            chat_id=chat_id
        )
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Chat not found")

    return MessageRead.model_validate(message)
