class Users():
	def __init__(self, first_name, last_name, age, location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
	
	def describe_user(self):
		print(
		    "Name: " +  self.first_name + ";" +
		    "\nLast name: " + self.last_name + ";" +
		    "\nAge: " + str(self.age) + ";" +
		    "\nLocation: " + self.location + "."
		    )
	def great_user(self):
		print("Hey, " + self.first_name + ", You are Great!\n")
