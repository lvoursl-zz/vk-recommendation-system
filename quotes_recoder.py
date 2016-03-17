


for i in range(1, 12175):
	try:
		users_file = open('users_data/' + str(i), 'r', encoding = 'cp1251').read()
		user_data = str(users_file).replace('"', "'")

		write_users_file = open('users_data/' + str(i), 'w')
		print(user_data, file = write_users_file)
		write_users_file.close()
		print(i)
	except Exception as e:
		print(str(e))
		pass
