import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items


blp = Blueprint("Items", __name__, description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Store not found")

    def delete():
        pass

    def put():
        pass

