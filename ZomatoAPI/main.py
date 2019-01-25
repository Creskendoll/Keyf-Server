from KeyfService import KeyfService
from ZomatoShop import ZomatoShop
import json
import io

service = KeyfService()
# data = service.readZomato()

# with open('data.json', 'w') as outfile:
#     json.dump(data, outfile)

with io.open('./data.json', mode='r', encoding='utf-8') as data:
    zomato_shops = json.load(data)
    zomato_shops = zomato_shops['restaurants']
    for shop_data in zomato_shops:
        zomato_shop = ZomatoShop(shop_data)
        service.writeShop(zomato_shop.toKeyfEntity())

