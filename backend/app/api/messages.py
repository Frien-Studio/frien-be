from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.db.models import Conversation, Message
from app.db.schemas import MessageCreate, MessageOut

router = APIRouter(
    prefix="/conversations/{conversation_id}/messages",
    tags=["messages"],
)

# endpoint for adding messages to db
@router.post(
    "",
    response_model=MessageOut,
    status_code=status.HTTP_201_CREATED,
)
def create_message(
    conversation_id: int,
    payload: MessageCreate,
    db: Session = Depends(get_db),
):
    # Ensure conversation exists
    conversation = (
        db.query(Conversation)
        .filter(Conversation.id == conversation_id)
        .first()
    )
    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found",
        )

    message = Message(
        conversation_id=conversation_id,
        role=payload.role,
        content=payload.content,
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    return message

# get endpoint for returning all messages of a conversation
@router.get("", response_model=list[MessageOut])
def get_messages(
    conversation_id: int,
    db: Session = Depends(get_db),
):
    # Ensure conversation exists
    conversation = (
        db.query(Conversation)
        .filter(Conversation.id == conversation_id)
        .first()
    )
    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found",
        )

    messages = (
        db.query(Message)
        .filter(Message.conversation_id == conversation_id)
        .order_by(Message.created_at)
        .all()
    )

    return messages
