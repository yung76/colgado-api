from pydantic import BaseModel, Field
from typing import Optional, List


class Save(BaseModel):
    id: Optional[int] = None
    in_progress_word: str
    word_complete: str
    try_number: int = Field(..., le=20)
    game_state: str
    user_id: int

    class Config:
        schema_extra = {
            "example": {
                "in_progress_word": "__a",
                "word_complete": "dia",
                "try_number": 3,
                "game_state": "in_progress/ended/won",
                "user_id": 1
            }
        }
