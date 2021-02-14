"""Импортирую родительский класс User, что бы подкласс Admin работал"""
from Users import Users

class Privileges():
	def __init__(self): 
		self.privileges = [
			'разрешено добавлять сообщения',
			'разрешено удалять пользователей',
			'разрешено банить  пользователей'
			]
	
	def show_privileges(self): 
		print(self.privileges)
		
class Admin(Users):
	def __init__(self, first_name, last_name, age, location):
		super().__init__(first_name, last_name, age, location)
		self.for_privileges = Privileges()
