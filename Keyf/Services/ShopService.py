from flask_restful import Resource
from Keyf import mongo
from flask import request, abort
from Keyf.Entities import Shop


class ShopService(Resource):
    def get(self, shop_id):
        """
        Returns the shop entry with id of shop_id.

            shop_id: string
            If the URL parameter shop id is -1 we return all the shops in the DB
            
            TODO: Return only the closest shops to the user
        """
        coffeshops = mongo.db.coffee_shops
        if shop_id == "-1":
            # Get all shops
            cursor = coffeshops.find({})
            # cast the data to CoffeeShop class
            shops_list = [Shop(data=shop).serialize() for shop in cursor]

            return {"shops": shops_list}
        else:
            # Get shops with id of shop_id
            cursor = coffeshops.find_one({"id": int(shop_id)})
            if cursor is not None:
                return Shop(cursor).serialize()
            return abort(404)  # Not found

    def put(self, shop_id):
        """
        Inserts a new entry to DB.
            TODO: The shop_id parameter is redundant and should be removed somehow.

            If there exists an entry with the same id then the existing entry is overwritten.

            TODO: Throw an error if the item trying to be created already exists in the DB. We should do the updating in POST.    
       
        """
        # DB connection
        shops_db = mongo.db.coffee_shops
        # The sent data is held in request.form
        # Cast the data to CoffeeShop object
        shop = Shop(data=request.form.to_dict())
        result = None
        try:
            # Add a new shop if the id is -1
            id_result = list(shops_db.find({}, {"id": 1}).sort([("id", -1)]).limit(1))
            # Create a new entry with a new id
            if not id_result:
                # If the DB is empty set the first shops id to 1
                shop.id = 1
            else:
                # TODO: We could implement an id with letter and number on the long run
                max_id = id_result[0]["id"]
                # Set the shop id
                shop.id = max_id + 1
            # Insert the new entry
            result = shops_db.insert_one(shop.serialize()).inserted_id
        except Exception as e:
            print("Error in CoffeeShopService PUT", e)
            return str(e), 500

        return {"shop_id": str(result), "operation_type": "insert"}

    def post(self, shop_id):
        """
            Update an existing entry

        """
        shops_db = mongo.db.coffee_shops

        shop = Shop(data=request.form.to_dict())
        try:
            # Overwrite the existing entry
            result = shops_db.replace_one(
                {"id": shop.id}, shop.serialize(), upsert=True
            ).upserted_id
        except Exception as e:
            print("Error in CoffeeShopService POST", e)
            return str(e), 500

        return {"shop_id": str(result), "operation_type": "replace"}

    def delete(self, shop_id):
        """
            Delete an entry, 404 if shop doesn't exist
        """
        shops_db = mongo.db.coffee_shops

        try:
            res = shops_db.find({"id": int(shop_id)})
            if len(list(res)) == 0:
                return abort(404)
            shops_db.delete_one({"id": int(shop_id)})
        except Exception as e:
            print("Error in DELETE shop", e)
            return str(e), 500

        return "OK", 200
