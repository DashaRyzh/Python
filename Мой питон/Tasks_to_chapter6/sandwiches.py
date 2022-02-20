sandwich_orders = ['mushroom', 'pastrami', 'becon', 'pastrami', 'salami', 'pastrami', 'cheeze']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
print(sandwich_orders)

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(f'Making {current_sandwich} sandwich')
	finished_sandwiches.append(current_sandwich)
print(f'Finished sandwiches: ')	
for sandwich in finished_sandwiches:	
	print(f'{sandwich} sandwich')