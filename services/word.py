from models.word import Word as WordModel
from schemas.word import Word


class WordService:

    def __init__(self, db) -> None:
        self.db = db

    def get_words(self):
        result = self.db.query(WordModel).all()
        return result

    def get_word(self, id):
        result = self.db.query(WordModel).filter(WordModel.id == id).first()
        return result

    def create_word(self, word: Word):
        new_user = WordModel(**word.dict())
        self.db.add(new_user)
        self.db.commit()
        return

    def update_word(self, id: int, data: Word):
        user = self.db.query(WordModel).filter(WordModel.id == id).first()
        user.email = data.email
        user.password = data.password
        self.db.commit()
        return

    def delete_word(self, id: int):
        self.db.query(WordModel).filter(WordModel.id == id).delete()
        self.db.commit()
        return
