def show_magicans(magicans):
	for magican in magicans:
		msg = "Is a magican " + magican.title() + "!"
		print(msg)
magicans = ["gudini", "copperfield", "messing"]
magicans1 = magicans[:]
def make_great(magicans):
	for i in range(len(magicans)): # переборка производится по индексам
		#элементов списка, которые соответствуют его длине
		magicans1[i] = "Great " + magicans[i]
	print(magicans1)
show_magicans(magicans)
make_great(magicans)
print(magicans)
print(magicans1)
