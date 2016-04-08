import pandas as pd
import ast

# коэффициент Танимото: чем ближе к 1, тем больше сходство между множествами
def tanamoto(vector1, vector2):
	c1, c2, shr = 0, 0, 0
	for i in range(len(vector1)):
		if (vector1[i] != 0) : c1 += 1
		if (vector2[i] != 0) : c2 += 1
		if (vector1[i] != 0) and (vector2[i] != 0) : shr += 1        
	return (float(shr) / (c1 + c2 - shr))


music_data_frame = pd.DataFrame(index = [1])
music_data_counter = 1

# получение данных о предпочтениях пользователя
with open('data_file', 'r', encoding = 'cp1251') as data_file:
	user_counter = 1
	for line in data_file:	
		try:			
			readed_data = line.lower()
			# преобразуем данные в словарь
			data = ast.literal_eval(readed_data)
			user_music = data
			#print(user_music)
			#user_music = data['response'][0]['music']
			#user_music = user_music.split(',')
			for artist in user_music:
				if (artist[0] == ' '): 
					artist = artist[1:]                
				if (artist not in music_data_frame.columns) and (len(str(artist)) < 20) and (len(str(artist)) > 2):
					music_data_frame[artist] = 0
					music_data_counter = music_data_frame.count(axis = 1)
					music_data_frame.loc[music_data_counter[1]] = 0
			
			for fix_artist in user_music:
				if (fix_artist[0] == ' '):
					fix_artist = fix_artist[1:]  
				for artist in user_music:
					if (artist[0] == ' '):
						artist = artist[1:]                
					
					if (fix_artist != artist) :            
						artist_index = music_data_frame.columns.get_loc(artist)
						fix_artist_index = music_data_frame.columns.get_loc(fix_artist)                   
						music_data_frame[artist][fix_artist_index + 1] += 1
						music_data_frame[fix_artist][artist_index + 1] += 1
	               
			user_counter += 1
			print(user_counter)
			if (user_counter > 50): break
		except Exception as e:
			#print('errrroooor ' + str(e))
			user_counter += 1
			continue


columns_num = music_data_frame.count(axis = 1)

# сгенерированый csv со всеми взаимосвязями
music_data_frame.to_csv('music_matrix.csv', encoding = 'cp1251')

# обрабатываем матрицу
df = pd.read_csv('music_matrix.csv', encoding = 'cp1251')
df.drop('Unnamed: 0', inplace = True, axis = 1)

#col_list = list(music_data_frame.columns.values)
#print(df[col][1]) 
#print(df.columns[1])    

