from models.save import Save as SaveModel
from schemas.save import Save


class SaveService:

    def __init__(self, db) -> None:
        self.db = db

    def get_saves(self):
        result = self.db.query(SaveModel).all()
        return result

    def get_user(self, id):
        result = self.db.query(SaveModel).filter(SaveModel.id == id).first()
        return result

    def create_save(self, save: Save):
        new_user = SaveModel(**save.dict())
        self.db.add(new_user)
        self.db.commit()
        return
