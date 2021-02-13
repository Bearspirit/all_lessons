""" Импортирую класс Admin из файла с тремя классами и вызываю
его метод"""

from Classes import Admin
my_self = Admin('Mikhail', 'Voytovich', 31, 'Kazan')
my_self.describe_user()
