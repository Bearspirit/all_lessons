ticket = "\nПожалуйста, введите свой возраст \nСкидка зависит от возраста: "
age = ""
while True:
	a = input(ticket)
	if int(a) < 3:
		print("Билет для Вас бесплатный")
	elif 3 <= int(a) < 12:
		print("Билет для Вас стоит 10 баксов")
	elif int(a) >= 12:
		print("Для Вас билет стоит 15 баксов")
	else:
		break
