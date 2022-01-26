countries = ['France', 'USA', 'India', 'China', 'Italia']
print(f'The original list: {countries}')
print(f'Soted list: {sorted(countries)}')
print(f'Sorted in reverse alphabetical order: {sorted(countries, reverse=True)}')
print(countries)
countries.reverse()
print(countries)
countries.sort()   # sort изменяет сам список, sorted просто разово выводит его в изменённом виде
print(countries)
countries.sort(reverse = True)
print(countries)
