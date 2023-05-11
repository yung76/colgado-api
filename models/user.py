from config.database import Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

    saves = relationship("save.Save", back_populates="user",lazy='dynamic')
