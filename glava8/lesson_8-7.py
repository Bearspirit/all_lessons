def make_album(name, album, track=''):
	forma = {'musican': name, 'sigle': album}
	if track:
		forma['dor'] = track
	return forma
func = make_album("Пикник", "Египтянин")
print(func)
