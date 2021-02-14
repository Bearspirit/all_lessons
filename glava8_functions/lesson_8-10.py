def show_magicans(magicans):
	for magican in magicans:
		msg = "Is a magican " + magican.title() + "!"
		print(msg)
magicans = ["gudini", "copperfield", "messing"]
def make_great(magicans):
	for i in range(len(magicans)): # переборка производится по индексам
		#элементов списка, которые соответствуют его длине
		magicans[i] = "Great " + magicans[i]
	print(magicans)
show_magicans(magicans)
make_great(magicans)
