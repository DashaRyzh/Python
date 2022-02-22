def sandwiches(*args):
	print(f'You ordered sandwich with:')
	for i in args:
		print(i)
		

sandwiches('cheese', 'tomatoes', 'cucumber')