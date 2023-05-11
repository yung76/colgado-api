from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Save(Base):
    __tablename__ = "saves"

    id = Column(Integer, primary_key=True)
    in_progress_word = Column(String)
    word_complete = Column(String)
    try_number = Column(Integer)
    game_state = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("user.User", back_populates="saves")
