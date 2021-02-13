"""Импортирую класс Admin из модуля, который ссылается на другой модуль
Users, так как является подклассом"""

from Adm_Priv import Privileges, Admin

my_self = Admin('Mikhail', 'Voytovich', 31, 'Kazan')
my_self.for_privileges.show_privileges()
