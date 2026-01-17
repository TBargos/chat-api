from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session

from app.database import get_session
from app.schemas.chat import ChatCreate, ChatRead
from app.crud import chats as chat_crud

router = APIRouter(prefix="/chats",tags=["chats"])


@router.post("/", response_model=ChatRead, status_code=201)
def create_chat(data: ChatCreate, session: Session = Depends(get_session)):
    chat = chat_crud.create_chat(session=session, data=data)
    return ChatRead.model_validate(chat)


@router.get("/{chat_id}", response_model=ChatRead)
def get_chat(chat_id: int, limit: int = Query(20, ge=1, le=100), session: Session = Depends(get_session)):
    chat = chat_crud.get_chat(
        session=session,
        chat_id=chat_id,
        limit=limit,
    )
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    return ChatRead.model_validate(chat)


@router.delete("/{chat_id}", status_code=204)
def delete_chat(chat_id: int, session: Session = Depends(get_session)):
    deleted = chat_crud.delete_chat(session=session, chat_id=chat_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Chat not found")