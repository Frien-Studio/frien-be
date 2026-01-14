from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# /users
class UserCreate(BaseModel):
    email: EmailStr
    name: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: str

    class Config:
        from_attributes = True  # SQLAlchemy → Pydantic

# /conversation
class ConversationCreate(BaseModel):
    user_id: int
    title: Optional[str] = None

class ConversationOut(BaseModel):
    id: int
    user_id: int
    title: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


# /message
class MessageCreate(BaseModel):
    role: str  # "user" | "assistant" | "system"
    content: str


class MessageOut(BaseModel):
    id: int
    conversation_id: int
    role: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True
