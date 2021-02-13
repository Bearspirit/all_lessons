def my_car(marka, model, **others):
	parameter = {}
	parameter['marka'] = marka
	parameter['model'] = model
	for key, value in others.items():
		parameter[key] = value
	return parameter
info = my_car('subaru', 'forester', motor='2.0', gear='manual',
				color='silver')
print(info)
 
