def city_country(city, country):
	text = city.title() +", " + country.title()
	return text
lesson = city_country("Berlin", "Germany")
print(lesson)
