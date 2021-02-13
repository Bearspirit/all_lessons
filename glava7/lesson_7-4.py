text_1 = "\nВыберите дополнение к пицце!"
text_1 += "\n(Если хотите завершить введите 'quit'): "
topping = ""
while topping != 'quit':
	topping = input(text_1)
	if topping != 'quit':
		print("Вы добавили " + topping.title() + "!")
