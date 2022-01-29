age = 30
human = ' '
if age < 2:
	human = 'baby'
elif age >= 2 and age < 4:
	human = 'child'
elif age >= 4 and age < 13:
	human = 'kid'
elif 13 <= age < 20:
	human = 'teenager'
elif age >= 20 and age < 65:
	human = 'adult'
else:
	human = 'old man'
print(f'You are a(n) {human}.')