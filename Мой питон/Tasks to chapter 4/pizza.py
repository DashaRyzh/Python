pizzas = ['4 cheeses', 'pepperoni', 'mushroom', 'margarita', 'chicken and mushrooms']
for pizza in pizzas:
	print(f'I like {pizza} pizza.')
print('I really like pizza!')
print('The first three items in the list are:')
print(pizzas[:3])
print('Three items from the middle of the list are:')
print(pizzas[1:4])
print('The last three items in the list are:')
print(pizzas[-3:])
friend_pizzas = pizzas[:]
pizzas.append('with pineapple')
friend_pizzas.append('with meat')
print('My favorite pizzas:')
for pizza in pizzas:
	print(pizza)
print('\n')
print("My friend's favotite pizzas:")
for pizza in friend_pizzas:
	print(pizza)