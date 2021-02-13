class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		print(self.restaurant_name + " " + self.cuisine_type)
		
	def open_restaurant(self):
		print("The " + self.restaurant_name.title() + " is open!")
	
my_restaurant = Restaurant("Shaurma", "Larek")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

