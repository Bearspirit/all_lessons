favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phill': 'python',
    }
persons = ['jen', 'sarah', 'edward', 'phill', 'tom', 'mark']
for name in persons:
	if name in favorite_languages.keys():
		print(name.title() + " spasibo")
	else:
		print(name.title() + " ty eto, davai")
 
