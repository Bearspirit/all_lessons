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

class Admin(Users):
	def __init__(self, first_name, last_name, age, location):
		super().__init__(first_name, last_name, age, location)
		self.privileges = [
			'разрешено добавлять сообщения',
			'разрешено удалять пользователей',
			'разрешено банить  пользователей'
			]
	def show_privileges(self):
		print(self.privileges)

my_self = Admin('Mikhail', 'Voitovich', 31, 'Kazan')
my_self.show_privileges()
