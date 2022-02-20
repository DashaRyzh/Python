num = {'Anton': {1, 3, 5, 7}, 'Dasha': {1, 5}, 'Varya': {1, 2, 3}, 'Sava': 7}

for person, numbers in num.items():
	print(f'{person} likes numbers: {numbers}')