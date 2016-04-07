import ast

data_file = open('data_file', 'a+')
counter = 0
#231473
for i in range(1, 231473):
	try:
		users_file = open('users_data/' + str(i), 'r', encoding = 'cp1251')
		readed_data = users_file.read()
		users_file.close()
		readed_data = readed_data.lower()

		# преобразуем данные в словарь
		data = ast.literal_eval(readed_data)
		user_music = data['response'][0]['music']
		user_music = user_music.split(',')
		if (len(user_music) > 1): 
			print(str(user_music), file = data_file)
			counter += 1
			print(counter)
	except Exception as e:
		#print(str(e))
		pass

#data_file1 = open('data_file', 'r', encoding = 'cp1251')
#print(str(data_file1.read()))