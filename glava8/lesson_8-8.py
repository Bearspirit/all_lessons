def make_album(name, album):
	forma = {'musican': name, 'sigle': album}
	return forma
while True:
	name_1 = input("\nMusican name: ")
	if name_1 == "q":
		break
	album_1 = input("Album name: ")
	if album_1 == "q":
		break
	func = make_album(name_1, album_1)
	print(func)
