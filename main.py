# Convert a comma-separated String to a Dictionary in Python

my_str = "name=Bobbby,country=Austria,language=German"

my_dict = dict(item.split('=') for item in my_str.split(','))

# 👇️ {'name': 'Bobbby', 'country': 'Austria', 'language': 'German'}
print(my_dict)