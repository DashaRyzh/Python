person = {'first_name': 'Anton', 'last_name': 'Ryzhikov', 'age': 29, 'city': 'Balashiha'}

# print(person['first_name'])
# print(person)
# print(person.get('age'))
# print(person.get('eye_color'))

# for key, value in person.items():
# 	print(f'\nKey: {key}')
# 	print(f'Value: {value}')

# for key in person.keys():
# 	print(key)

# keys = ['first_name', 'age']  # поиск по определённым ключам
# for value in person.keys():  # можно использовать с командой sorted => sorted(person.keys())
# 	if value in keys:
# 		current_value = person[value]
# 		print(value, current_value)

for value in person.values():
	print(value)