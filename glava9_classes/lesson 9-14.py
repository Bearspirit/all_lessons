"""Имитация бросания кубиков"""

from random import randint

class Die():
    def __init__(self, sides=6):
        """Класс содержит один атрибут со значением по умолчанию (число граней кубика)"""
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(x)

    def imitation(self):
        for i in range(0, self.sides):
            self.roll_die()
        
     def in_tuple(self):
         x = []
         x.append(self.imitation())
         print(x)


cub_6 = Die(6)
cub_6.in_tuple()