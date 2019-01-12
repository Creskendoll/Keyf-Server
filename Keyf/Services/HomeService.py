from flask_restful import Resource
from Keyf import mongo
from flask import send_from_directory

class HomeService(Resource):
    def get(self):
        return send_from_directory('.', 'index.html')