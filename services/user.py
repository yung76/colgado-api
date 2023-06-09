from models.save import Save as SaveModel
from models.user import User as UserModel
from schemas.user import User


class UserService:

    def __init__(self, db) -> None:
        self.db = db

    def get_users(self):
        result = self.db.query(UserModel).all()
        return result

    def get_user(self, id):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        return result

    def create_user(self, user: User):
        new_user = UserModel(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        return

    def update_user(self, id: int, data: User):
        user = self.db.query(UserModel).filter(UserModel.id == id).first()
        user.email = data.email
        user.password = data.password
        self.db.commit()
        return

    def delete_user(self, id: int):
        self.db.query(UserModel).filter(UserModel.id == id).delete()
        self.db.commit()
        return
