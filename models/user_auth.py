from db import db


class UserAuth(db.Model):
    __tablename__ = "user_auth"

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(120), unique=True, nullable=False)
    