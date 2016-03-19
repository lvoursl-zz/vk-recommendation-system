import pandas as pd
import ast

music_data_frame = pd.DataFrame(index = [1])
music_data_counter = 0

# получение данных о предпочтениях пользователя
user_counter = 1
while user_counter != 500:
	try:
		users_file = open('users_data/' + str(user_counter), 'r', encoding = 'cp1251')
		readed_data = users_file.read()
		users_file.close()

		readed_data = readed_data.lower()

		# куча реплейсов, т.к. ни один парсер адекватно не рашет проблем с кавычками
		readed_data = readed_data.replace("'tv': '", '"tv": "')
		readed_data = readed_data.replace("', 'games': '", '", "games": "')
		readed_data = readed_data.replace("', 'music': '", '", "music": "')
		readed_data = readed_data.replace("', 'books': '", '", "books": "')
		readed_data = readed_data.replace("', 'movies': '", '", "movies": "' )
		readed_data = readed_data.replace("', 'activities': '", '", "activities": "')
		readed_data = readed_data.replace("', 'uid':", '", "uid":')
		readed_data = readed_data.replace("'first_name': '", '"first_name": "')
		readed_data = readed_data.replace("', 'interests': '", '", "interests": "')
		readed_data = readed_data.replace("', 'last_name': '", '", "last_name": "')
		readed_data = readed_data.replace("'}]", '"}]')

		# удаляем мешающие обратке скобки 
		readed_data = '' + readed_data[1:]
		readed_data = readed_data[:len(readed_data) - 4] + ''

		# преобразуем данные в словарь
		data = ast.literal_eval(readed_data)

		user_music = data['music'].split(',')

		for artist in user_music:
			
			if (artist not in music_data_frame.columns) and (len(str(artist)) < 20):				
				
				if (artist[0] == ' '):
					music_data_frame[artist[1:]] = 0					
				else:
					music_data_frame[artist] = 0

				

		user_counter += 1

	except Exception as e:
		#print(str(e))
		user_counter += 1
		continue


columns_num = music_data_frame.count(axis = 1)

#print(music_data_frame.columns)
print(columns_num[1])
print(music_data_counter)
# генерируем нужны колонки
#for i in range(2, columns_num[1]):
#	music_data_frame.loc[i] = 0

# сгенерированый csv со всеми взаимосвязями
music_data_frame.to_csv('music_matrix.csv', encoding = 'cp1251')


df = pd.read_csv('music_matrix.csv', encoding = 'cp1251')
cn = df.count(axis = 1)
# получаем имя колонки (queen - в данном случае)
name = df.columns[1]
print(df.columns[1])
#print((df.columns == name).nonzero())

'''
music_data_frame.to_csv('music_matrix.csv')

#print(music_data_frame.drop(music_data_frame.columns))

writer = pd.ExcelWriter('output.xlsx')
music_data_frame.to_excel(writer,'Sheet1')
writer.save()
'''