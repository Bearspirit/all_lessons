sandwich_orders = ['pastrami', 'burger', 'pastrami', 'sprotes', 'pastrami', 'salat']
print(sandwich_orders)
print("Pastrami is not in list!")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
	print(sandwich_orders)
print(sandwich_orders)
