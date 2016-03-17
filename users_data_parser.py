'''import json
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
'''
import json 
from urllib.request import urlopen

'''users_file = open('users_data/2617', 'r', encoding = 'cp1251')
json_users_data = json.load(users_file)
#print(json_users_data[0]['movies'])
'''

token = '4f318b471cda5c6bd6337cfc2644b478038ee7bb09a6158395101a036b834fc315c19b3fec6b9e28ea370'
users_counter = 1


request = urlopen('https://api.vk.com/method/users.get?user_ids=' + str(users_counter) + '&fields=activities,interests,music,movies,tv,books,games' + '&access_token=' + token).read()
data = json.loads(str(eval(request)))

users_file = open('1.json', 'w')
print(data, file = users_file)
users_file.close()

users_file = open('1.json', 'r', encoding = 'cp1251')
json_users_data = json.load(str(users_file))
print(json_users_data[0]['movies'])