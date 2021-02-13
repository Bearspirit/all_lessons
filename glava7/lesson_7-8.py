sandwich_orders = ['burger', 'sprotes', 'salat']
finished_sandwiches = []
while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print("I made your " + sandwich.title() + " sandwich")
	finished_sandwiches.append(sandwich)
for i in finished_sandwiches:
	print("For you " + i + " !")
print(finished_sandwiches)
print(sandwich_orders)
