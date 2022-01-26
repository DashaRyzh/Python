cubes = []
for num in range(1, 11):
	cubes.append(num ** 3)
	print(num ** 3)

cubes1 = [num ** 3 for num in range(1, 11)]
print(cubes1)