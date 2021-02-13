class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		print(self.restaurant_name + " " + self.cuisine_type)
		
	def open_restaurant(self):
		print("The " + self.restaurant_name.title() + " is open!")
	
my_restaurant = Restaurant("Shaurma", "Larek")
you_restaurant = Restaurant("Kebab", "Palatka")
our_restaurant = Restaurant("Shashlyk", "Mangal")

my_restaurant.describe_restaurant()
you_restaurant.describe_restaurant()
our_restaurant.describe_restaurant()
