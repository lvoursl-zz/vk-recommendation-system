import pandas as pd
import ast

artists = []
music_data_frame = pd.DataFrame(index = [0])

# получение данных о предпочтениях пользователя
user_counter = 1
while user_counter != 500:
	try:
		users_file = open('users_data/' + str(user_counter), 'r', encoding = 'cp1251')
		readed_data = users_file.read()
		users_file.close()

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


		readed_data = '' + readed_data[1:]
		readed_data = readed_data[:len(readed_data) - 4] + ''

		data = ast.literal_eval(readed_data)

		user_music = data['music'].split(',')

		for artist in user_music:
			if artist not in artists:
				if artist[0] == ' ':
					artists.append(artist[1:])
				else:
					artists.append(artist)

			if artist not in music_data_frame.columns:
				if (artist[0] == ' ') and (len(str(artist)) < 20):
					music_data_frame[artist[1:]] = 0
				else:
					music_data_frame[artist] = 0

		user_counter += 1


		# при обработке не забыть выставить ограничение на длину названия
	except Exception as e:
		print(str(e))
		user_counter += 1
		continue


artists_file = open('artists', 'w+')
print(artists, file = artists_file)

#print(music_data_frame.drop(music_data_frame.columns))

writer = pd.ExcelWriter('output.xlsx')
music_data_frame.to_excel(writer,'Sheet1')
writer.save()