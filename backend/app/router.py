from fastapi import FastAPI
from app.api.users import router as users_router
from app.api.conversations import router as conversations_router
from app.api.messages import router as messages_router

app = FastAPI()

app.include_router(users_router)
app.include_router(conversations_router)
app.include_router(messages_router)