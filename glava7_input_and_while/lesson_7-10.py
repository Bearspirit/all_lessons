dreams = {}
b = True
while b:
	name = input("Введите ваше имя :")
	location = input("Введите место, в котором хотели бы отдохнуть: ")
	dreams[name] = location
	a = input("Продолжить опрос? (да/нет): ")
	if a == 'нет':
		b = False
print("\n---Итоги опроса---")
for name, location in dreams.items():
	print(name + " мечтате отдохнуть в " + location)
