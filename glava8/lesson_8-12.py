def sandwiches(*toppings):
	print("\nВы выбрали следующий сандвич: ")
	for i in toppings:
		print("\n" + "- " + i)
sandwiches("Рыбный")
