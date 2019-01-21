from Keyf.Entities import DBEntity

class CoffeeShop(DBEntity):
    def __init__(self, data={}):
        if 'id' in data:
            self.id = data['id']
        else:
            self.id = -1
        if 'name' in data:
            self.name = data['name']
        else:
            self.name = ""
        if 'photo' in data:
            self.photo = data['photo']
        else:
            self.photo = "http://savoryconceptsllc.com/wp-content/uploads/2016/05/question-mark-png-5a381257a89243.6425987715136241516905-1.jpg"
        if 'menu' in data:
            self.menu = data['menu']
        else:
            self.menu = {
                "coffees_menu": [],
                "desserts_menu": [],
                "dayspecial_menu": []
            }
        if 'location' in data:
            self.location = data['location']
        else:
            self.location = {
                "lat": 0,
                "long": 0
            }
        if 'reviews' in data:
            self.reviews = data['reviews']
        else:
            self.reviews = []
        if 'working_hours' in data:
            self.working_hours = data['working_hours']
        else:
            self.working_hours = {
                "opening": "08:00",
                "closing": "01:00"
                }
        if 'rating' in data:
            self.rating = data['rating']
        else:
            self.rating = 0.0

    def serialize(self):
        obj = {
            "id": self.id,
            "name": self.name,
            "photo": self.photo,
            "menu": self.menu, 
            "location": self.location,
            "reviews": self.reviews,
            "working_hours":self.working_hours,
            "rating": self.rating
        }
        return obj
