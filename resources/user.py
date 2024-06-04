from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from passlib.hash import pbkdf2_sha256

from db import db
from models import UserModel
from schemas import UserSchema

blp = Blueprint("Users", "users", operations="Operations on user")


@blp.rout("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409, "An user with that username already exists")
        
        user = UserModel(
            username=user_data["username"],
            password=pbkdf2_sha256.hash(user_data["password"])
        )
        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully."}, 201


@blp.rout("/user/<int:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)

        return user
