from urllib.request import urlopen
from time import sleep 

token = '4f318b471cda5c6bd6337cfc2644b478038ee7bb09a6158395101a036b834fc315c19b3fec6b9e28ea370'
users_counter = 1322

#users_file = open('users_data/1', 'r', encoding='cp1251').read()
#print((users_file))


while users_counter < 10000:
	try:
		print('downloaded ' + str(users_counter) + ' users')
		users_counter += 1
		request = urlopen('https://api.vk.com/method/users.get?user_ids=' + str(users_counter) + '&fields=activities,interests,music,movies,tv,books,games' + '&access_token=' + token)
		data = eval(request.read())	

		users_file = open('users_data/' + str(users_counter), 'w')
		print(str(data['response']), file = users_file)
		users_file.close()

		sleep(2)		
	except Exception as e:
		print(str(e))
		pass




#request = urlopen('https://api.vk.com/method/users.get?user_ids=1&fields=activities,interests,music,movies,tv,books,games')
#data = eval(request.read())	

#print(data['response'][0])