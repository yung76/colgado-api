from pydantic import BaseModel
from typing import Optional


class Word(BaseModel):
    id: Optional[int] = None
    word: str

    class Config:
        schema_extra = {
            "example": {
                "word": "palabra"
            }
        }
