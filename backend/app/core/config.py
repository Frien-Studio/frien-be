from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseModel):
    DATABASE_URL: str

settings = Settings(
    DATABASE_URL=os.getenv("DATABASE_URL"),
)
