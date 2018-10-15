import json
from auth import *
import hashlib
import sys


	
	
	
def encode(user_password):
	hash_object = hashlib.sha256(user_password.encode())
	hex_dig = hash_object.hexdigest()
	return hex_dig
	
	
	
	
def check_if_stored_master_password():
	with open('master_password.json') as master_password_data:
		master_password_stored_data = json.load(master_password_data)
	masterPasswordStored = "" in master_password_stored_data
	if masterPasswordStored == True:
		pass
	else:
		print("There is no master password stored. Create one now. ")
		storeANewPassword = input("Enter a new password: ")
		storeANewPassword2 = input("Re-enter the password: ")
		if storeANewPassword != storeANewPassword2:
			print("The passwords do not match.")
			sys.exit()
		else:
			hashed_master_password = encode(storeANewPassword)
			with open('master_password.json', 'w') as storeANewMasterPassword:
				new_stored_master_password = json.dump(hashed_master_password, storeANewMasterPassword)
			print("The password was saved. Restart the program to continue")
			sys.exit()
	
def check_if_stored_regular_password():
	with open('password.json') as password_data:
		password_stored_data = json.load(password_data)
	passwordStored = "" in password_stored_data
	if passwordStored == True:
		pass
	else:
		print("There is no password stored. Create one now. ")
		storeANewPassword = input("Enter a new password: ")
		storeANewPassword2 = input("Re-enter the password: ")
		if storeANewPassword != storeANewPassword2:
			print("The passwords do not match.")
			sys.exit()
		else:
			hashed_password = encode(storeANewPassword)
			with open('master_password.json', 'w') as storeANewPassword:
				new_stored_master_password = json.dump(hashed_password, storeANewPassword)
			print("The password was saved. Restart the program to continue")
			sys.exit()