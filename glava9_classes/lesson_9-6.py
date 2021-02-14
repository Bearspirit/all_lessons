class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 5
	
	def describe_restaurant(self):
		print(self.restaurant_name + " " + self.cuisine_type)
		
	def open_restaurant(self):
		print("The " + self.restaurant_name.title() + " is open!")
		
	def set_number_served(self):
		print("Served peoples is " + str(self.number_served) + " !")
		
	def increment_number_served(self, peoples):
		self.number_served += peoples


class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['banana', 'strawberry', 'milk']
	def type_of_flavors(self):
		print(self.flavors)
		
my_cream = IceCreamStand('Ice cream', 'box')
my_cream.type_of_flavors()
