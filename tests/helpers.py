from Keyf.Entities import Shop, MenuItem, Review, User


def createShop(id):
    menu_item = MenuItem({"id": 0, "name": "Test item", "price": 100})
    review = Review({"rating": 3, "text": "Very nice",})
    data = {
        "id": id,
        "name": "test shop",
        "image": "http://savoryconceptsllc.com/wp-content/uploads/2016/05/question-mark-png-5a381257a89243.6425987715136241516905-1.jpg",
        "menu": [menu_item.serialize(), menu_item.serialize(), menu_item.serialize()],
        "location": {"lat": 1, "long": 1},
        "reviews": [review.serialize(), review.serialize()],
        "working_hours": {"opening": "09:00", "closing": "02:00"},
        "rating": 4.3,
    }
    return Shop(data)


def createUser(id):
    data = {
        "id": id,
        "name": "Kenan",
        "photo": "http://1.bp.blogspot.com/_Db02u7w1G7A/TJE-M2XO1iI/AAAAAAAADdE/oUUo-FJxOec/s1600/angry-dog1.jpg",
        "lists": {
            "favorite_shops": [1, 2, 3],
            "favorite_items": [3, 5, 6],
            "wish_list": [6, 8, 4],
        },
    }
    return User(data)

