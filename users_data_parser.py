import json
from pymongo import MongoClient

#users_file = open('users_data/11391', 'r', encoding = 'cp1251')
#json_users_data = json.load(users_file)
#print(json_users_data[0]['first_name'])

client = MongoClient('localhost', 27017)
db = client['vk-recommendation-system']
movies_collection = db['movies_collection']

print(db.collection_names())

#db = client.primer
#print(db.collection_names())
