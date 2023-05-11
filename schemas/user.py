from pydantic import BaseModel, Field, EmailStr, SecretStr
from typing import Optional


class User(BaseModel):
    id: Optional[int] = None
    email: EmailStr
    password: str = Field(min_length=3, max_length=10)

    class Config:
        schema_extra = {
            "example": {
                "email": "asd@asd.cl",
                "password": "Tu password"
            }
        }
