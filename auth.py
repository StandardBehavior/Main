# Authentication between programs

import random
from random import randint
import json



# Function to get auth pin

def get_auth_code(n):
	range_start = 10**(n-1)
	range_end = (10**n)-1
	return randint(range_start, range_end)

def store_auth_code():
	with open('auth.json', 'w') as auth_object:
		auth_code = json.dump(str(get_auth_code(6)), auth_object)
	
	


