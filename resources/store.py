import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores


blp = Blueprint("stores", __name__, description="Operations on stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self):
        pass

    def delete(self):
        pass
