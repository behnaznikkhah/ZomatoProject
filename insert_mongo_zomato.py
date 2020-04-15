import requests
from pprint import pprint
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Zomato"]
collection = database["Restaurants"]
header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": "XXXX"}
file = open("\root\Testlatlon.txt", "r")
counter = 0
for value in file:
    cordinates = value.split(",")
    print(cordinates)
    latitude = cordinates[0]
    longitude = cordinates[1]
    url = "https://developers.zomato.com/api/v2.1/geocode?lat=" +latitude + "&lon=" +longitude 
    print(url)
    response = requests.get(url, headers=header)
    data = response.json()
    for p in data['nearby_restaurants']:
        dict = {'_id':counter} 
        p.update(dict)
        x = collection.insert_one(p)
        counter = counter + 1

print("Data insert successful")