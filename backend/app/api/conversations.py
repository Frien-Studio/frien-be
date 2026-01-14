from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.db.models import Conversation, User
from app.db.schemas import ConversationCreate, ConversationOut

router = APIRouter(prefix="/conversations", tags=["conversations"])

@router.post(
    "",
    response_model=ConversationOut,
    status_code=status.HTTP_201_CREATED,
)
def create_conversation(
    payload: ConversationCreate,
    db: Session = Depends(get_db),
):
    # Ensure user exists
    user = db.query(User).filter(User.id == payload.user_id).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    conversation = Conversation(
        user_id=payload.user_id,
        title=payload.title,
    )

    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    return conversation
