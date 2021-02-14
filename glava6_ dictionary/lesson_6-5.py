rivers = {'nile':'egipt', 'volga': 'russia', 'amazonka': 'brazil'}
for key, value in rivers.items():
	print("The " + key.title() + " runs throgh " + value.title())
for key in rivers.keys():
	print(key.title())
for value in rivers.values():
	print(value.title())
