from flask_restful import Resource
from Keyf import mongo
from flask import request
from Keyf.Entities import User


class UsersService(Resource):
    def get(self, user_id):
        users = mongo.db.users
        if user_id == "-1":
            cursor = users.find({})
        else:
            cursor = users.find({"id": id})
        user_list = [User(data=user).serialize() for user in cursor]

        return {"users": user_list}

    def put(self, user_id):
        users = mongo.db.users
        user = User(data=request.form.to_dict())
        result = users.replace_one(
            {"id": user.id}, user.serialize(), upsert=True
        ).upserted_id

        if result is None:
            return {"user_id": user.id, "operation_type": "replace"}
        else:
            return {"user_id": user.id, "operation_type": "insert"}

    def post(self):
        pass

    def delete(self):
        pass
