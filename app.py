import uuid
from flask import Flask, request
from flask_smorest import abort
from db import stores, items

app = Flask(__name__)

@app.get("/store")
def get_stores():
    return  {"stores": stores}

@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4.hex
    new_store = {**store_data, "id": store_id}
    stores[store_id] = new_store
    return new_store, 201

@app.post("/item")
def create_item(name):
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        abort(404, message="Store not found")
    item_id = uuid.uuid4.hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    return item, 201
    
@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found")

@app.get("/item/<string:item_id>")
def get_item_in_store(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Store not found")