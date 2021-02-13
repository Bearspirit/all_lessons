class Users():
	def __init__(self, first_name, last_name, age, location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
		self.login_attempts = 0
	
	def describe_user(self):
		print(
		    "Name: " +  self.first_name + ";" +
		    "\nLast name: " + self.last_name + ";" +
		    "\nAge: " + str(self.age) + ";" +
		    "\nLocation: " + self.location + "."
		    )
	def great_user(self):
		print("Hey, " + self.first_name + ", You are Great!\n")
		
	def increment_login_attempts(self):
		self.login_attempts +=  1
		
	def reset_login_attempts(self):
		self.login_attempts = 0
		
"""		
i_self = Users("Mikhail", "Voitovich", 31, "Kazan")
i_self.describe_user()
i_self.great_user()

my_wife = Users("Diana", "Voitovich", 31, "Usady")
my_wife.describe_user()
my_wife.great_user()

my_brother = Users("Dmitriy", "Voitovich", 28, "Aviastroy")
my_brother.describe_user()
my_brother.great_user()
"""
new_user = Users("Mikhail", "Voitovich", 31, "Kazan") 
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
print(new_user.login_attempts)
new_user.reset_login_attempts()
print(new_user.login_attempts)  
