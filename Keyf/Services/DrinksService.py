from flask_restful import Resource
from Keyf import mongo
from flask import request
from Keyf.Entities import MenuItem

class DrinksService(Resource):
    def get(self, drink_id):
        coffeshops = mongo.db.drinks
        if drink_id == "-1":
            cursor = coffeshops.find({})
        else:
            cursor = coffeshops.find({"id": drink_id})    
        drinks_list = [MenuItem(data=drink).serialize() for drink in cursor]

        return {'drinks': drinks_list}

    def put(self, shop_id):
        drinks = mongo.db.drinks
        drink = MenuItem(data=request.form.to_dict())
        result = drinks.replace_one({"id": drink.id}, drink.serialize(), upsert=True).upserted_id

        if result is None:
            return { "shop_id": drink.id, "operation_type": "replace" }
        else:
            return { "shop_id": drink.id, "operation_type": "insert" }

    def post(self):
        pass
    def delete(self, shop_id):
        pass
