from flask_restful import Resource
from Keyf import mongo
from flask import Markup

class Home(Resource):
    def get(self):
        return Markup("<html><h1>Welcome to Keyf<h1></html>")