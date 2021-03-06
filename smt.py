from Keyf.Entities import Shop, MenuItem, Review
import pprint

menu_item = MenuItem({
        "id" : 0,
        "name" : "Test item",
        "price" : 100
    })
review = Review({
    "rating" : 3,
    "text" : "jshdgfkjshgdkjh gajhg sdkj ghk jahk jahsdg k ghs sdhj gdaksjh gafs"
})
data = {
    "id" : 0,
    "name" : "test shop",
    "image" : "http://savoryconceptsllc.com/wp-content/uploads/2016/05/question-mark-png-5a381257a89243.6425987715136241516905-1.jpg",
    "menu" : [
        menu_item.serialize(),
        menu_item.serialize(),
        menu_item.serialize()
    ],
    "location" : {"lat": 1, "long": 1},
    "reviews" : [
        review.serialize(),
        review.serialize()
    ],
    "working_hours" : {
        "opening" : "09:00",
        "closing" : "02:00"
    },
    "rating" : 4.3
}
shop = Shop(data)

pprint.pprint(shop.serialize())
