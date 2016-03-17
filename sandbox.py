import json
import re
import yaml

# как читать данные из "кривых" джейсон файлов

users_file = open('users_data/8422', 'r', encoding = 'cp1251')
readed_data = users_file.read()
try:
	data = json.loads(json.dumps(eval(readed_data)))
except Exception as e:
	print(str(e))
	#print(type(readed_data))
	'''readed_data = readed_data.replace("'", '"')
	print(readed_data)'''
	print(yaml.load(readed_data))
