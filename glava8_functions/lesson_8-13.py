def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
my_users = build_profile('mikhail', 'voitovich', city='kazan',
						age='31', job='KKM')
print(my_users)
