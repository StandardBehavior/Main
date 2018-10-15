# Main app with secure login authentication

import base64
import json
import time
import sys
import random
from random import randint
from auth import get_auth_code
from auth import store_auth_code
from check import *
import hashlib


# DEVELOPMENT MODE
# Set to False to ENABLE 2FA
developmentMode = False


# Functions
# Encoding Function
def encode(user_password):
	hash_object = hashlib.sha256(user_password.encode())
	hex_dig = hash_object.hexdigest()
	return hex_dig

# Open files
# Check how many times the program has been run
with open('program_data.json') as program_data_object:
	stored_program_data = json.load(program_data_object)
	

# Open Username and Password Files

with open('username.json') as x:
	stored_username = json.load(x)
		
with open('password.json') as c:
	stored_password = json.load(c)
		
# Open Master Username and Password files
with open('master_username.json') as a:
	stored_master_username = json.load(a)
	
with open('master_password.json') as b:
	stored_master_password = json.load(b)

	

# Set the master account to false
master_account = False	
		
# Set the password retries to 0 because the user hasn't entered their password yet
retries = 0

# Decide to set custom pin_enable to on or off
pin_enable = False



# Let the user enter their id
first_id = input("ID: ")
if first_id == stored_master_username:
	pass
		
		
# If the first_id variable doesn't match the master_id or the stored_username, produce an error
if first_id != stored_master_username and first_id != stored_username:
	user_id = input("Try again: ")
	if user_id != stored_username and user_id != stored_master_username:
		# If the id does not match the one in the JSON file, offer to create an account
		print("That login ID does not exist")
		quit()

				
			
# Offer to enter password
first_password = input("Password: ")

# Encode the password, then see if it matches
user_encoded_pass = encode(first_password)

	
if first_password == str('adminnokey') and first_id == stored_master_username:
	valid = False
	print("not valid")
	print("Welcome, Imposter.")
	# If both the id and password match the master account settings, set account to activated (True)
	master_account = False

if user_encoded_pass == stored_master_password and first_id == stored_master_username and developmentMode == True:
	valid = True
	master_account = True

	
if user_encoded_pass == stored_master_password and first_id == stored_master_username and developmentMode == False:
		
	# Master User Authentication
	valid = False

	store_auth_code()

	# Check the auth code 
	with open('auth.json') as auth_check:
		stored_auth_code = json.load(auth_check)
	
	print("Enter a valid key: ")
	auth = input()
	if auth != stored_auth_code:
		program_restarts = float(stored_program_data) + 1
		with open('program_data.json', 'w') as program_data_object:
			stored_program_data = json.dump(program_restarts, program_data_object)
		with open('data.txt', 'a') as data_object:
			data_object.write("\n")
			data_object.write("New user attempt on: ")
			data_object.write(time.strftime('%a %b %d'))
			data_object.write("\n")
			data_object.write("This was at: ")
			data_object.write(time.strftime('%T'))
		sys.exit("INVALID KEY")
	elif auth == stored_auth_code:
		store_auth_code()
		print("valid")
		# Set the valid variable to true
		valid = True
	else:
		sys.exit("FATAL ERROR")
	if valid == True:
		if pin_enable == True:
			master_pin = "528491"
			askForPin = input("PIN:  ")
			if askForPin != master_pin:
				print("incorrect")
				quit()
			else:
				pass
				print("Welcome, Master.")
				# If the ID, password, PIN, and Key match the master account settings, set account to activated (True)
				master_account = True
		elif pin_enable == False:
			print("Welcome, Master.")
			# If both the id and password match the master account settings, set account to activated (True)
			master_account = True
		else:
			sys.exit("FATAL ERROR")
			
	elif valid == False:
		print("ERROR")
		quit()
		
		
		
if user_encoded_pass != stored_master_password and user_encoded_pass != stored_password and first_password != str('adminnokey'):
	# If the password doesn't match the stored password, let them retry 3 times
	if user_encoded_pass != stored_password:
		print("Incorrrect password")
		print("Try again")
		while retries < 4:
			password_retry = input("Enter your password: ")
			encoded_password_retry = encode(password_retry)
			if encoded_password_retry == stored_password and master_account == False:
				print("SUCCESS")
				break
			else:
				print("FAIL")
				retries += 1
			# Exit after 3 failures
			program_restarts = float(stored_program_data) + 1
			with open('program_data.json', 'w') as program_data_object:
				stored_program_data = json.dump(program_restarts, program_data_object)
			sys.exit("You failed to enter your password correctly. Goodbye")

# End login module
		
# Begin Main˙ Program

# Open the JSON file to grab the balance
with open('balance.json') as balance_object:
	stored_balance = json.load(balance_object)
	
	


# Simulate loading
print("......")	
time.sleep(0.5)


# Start program

# Create a while loop to simulate a running program





# Options
# 1. Bank
# 2. Goals
# 3. Journal
# 4. Account
# 5. Settings





while True:
	if master_account == True:
		print("Choose an option: ")
		print("\n" + "(1) Bank" + "\n" + "(2) Goals" + "\n" + "(3) Journal" + "\n" + "(4) Account" + "\n" + "(5) Settings" + "\n" + "(6) Quit")
		print("\n")
		master_options = input()
		
		# Start if-else options
		if master_options == str(1):
			while True:
				# Bank
				print("Choose an option: ")
				print("\n" + "(1) Deposit" + "\n" + "(2) Withdraw" + "\n" + "(3) Overwrite balance" + "\n" + "(4) View Balance" + "\n" + "(5) Quit")
				bank_options = input()
				if bank_options == str(1):
					# Deposit
					print("Great! Please enter the value you wish to depost below: ")
					deposit_ammount = input("Enter a value: ")
					total_deposit = float(stored_balance) + float(deposit_ammount)
					with open("balance.json", "w") as x:
						total_deposit_stored = json.dump(total_deposit, x)
					if valid == True:
						print("Your new total is: " + str(total_deposit))
						continue
					else:
						print("You deposited: " + str(deposit_ammount))
						continue
					# Done Deposit
					finish = input("Done with bank? (y/n)  ")
					if finish == str('y'):
						break
					else:
						continue
				elif bank_options == str(2):
					# Withdraw
					print("hmmm... okay. Enter how much you took below: ")
					withdraw_amount = input("Enter a value: ")
					total_withdraw = float(stored_balance) - float(withdraw_amount)
					with open('balance.json', 'w') as c:
						total_withdraw_stored = json.dump(total_withdraw, c)
					if valid == True:
						print("Your new total is: " + str(total_withdraw))
						continue
					else:
						print("You withdrew: " + str(deposit_ammount))
						continue
					# Done withdraw
					finish = input("Done with bank? (y/n)  ")
					if finish == str('y'):
						break
					else:
						continue
					
				elif bank_options == str(3):
					# Overwrite Balance
					print("This will overwrite your current balance.")
					proceed = input("Proceed? (y/n)  ")
					if proceed == str('y'):
						ask_for_master_pass = input("Enter the Master Password to continue: ")
						check_master_pass = encode(ask_for_master_pass)
						if check_master_pass != stored_master_password:
							print("That was incorrect")
							continue
						new_stored_balance = input("Enter a new total balance: ")
						with open("balance.json", "w") as new_balance:
							final_stored_new_balance = json.dump(new_stored_balance, new_balance)
					else:
						continue
					# Done Overwrite balance
					finish = input("Done with bank? (y/n)  ")
					if finish == str('y'):
						break
					else:
						continue
				elif bank_options == str(4):
					print("The current balance is: " + stored_balance)
					input("Press enter to continue      ")
					continue
				elif bank_options == str(5):
					# Quit
					break
				else:
					continue	
				
		elif master_options == str(2):
			# Goals
			while True:
				print("Choose an option: ")
				print("\n" + "(1) Add a goal" + "\n" + "(2) Complete a goal" + "\n" + "(3) Quit")
				goal_options = input()
				if goal_options == str(1):
					# Add a goal
					print("Okay! Great!")
					add_goal = input("Type your goal: ")
					with open('goals.txt', 'a') as goals_file_object:
						goals_file_object.write("\n")
						goals_file_object.write(add_goal)
					finish = input("Done with goals? (y/n)  ")
					if finish == str('y'):
						break
					else:
						continue
					# end Add a goal
				elif goal_options == str(2):
					# Complete goal
					print("Awesome! Which goal did you finish? ")
					finished_goal_title = input("Enter the goal: ")
					more_goal_info = input("Enter more info about the goal! ")
					with open('goals.txt', 'a') as goals_file_object:
						goals_file_object.write("\n")
						goals_file_object.write(finished_goal_title)
						goals_file_object.write("\n")
						goals_file_object.write(more_goal_info)
					# end Complete goal
					finish = input("Done with goals? (y/n)  ")
					if finish == str('y'):
						break
					else:
						continue
				elif goal_options == str(3):
					# Quit
					break

				
		elif master_options == str(3):
			# Journal
			while True:
				print("Choose an option: ")
				print("\n" + "(1) Add an entry" + "\n" + "(2) Quit")
				journal_options = input()
				if journal_options == str(1):
					# Start add an entry
					entry_title = input("Enter a title: ")
					entry_body = input("Enter your body text: ")
					with open('journal.txt', 'a') as journal_object:
						journal_object.write("\n")
						journal_object.write(entry_title)
						journal_object.write("\n")
						journal_object.write(entry_body)
						journal_object.write("\n")
					# End add an entry
					finish = input("Done with goals? (y/n)  ")
					if finish == str('y'):
						break
					else:
						continue
				elif journal_options == str(2):
					break
		elif master_options == str(4):
			# Account
			while True:
				print("Choose an option: ")
				print("\n" + "(1) Change login ID" + "\n" + "(2) Change password" + "\n" + "(3) Quit")
				account_options = input()
				if account_options == str(1):
					print("OK. Please enter a new ID below: ")
					if master_account == True:
						ask_for_master_pass = input("Enter the Master Password to continue: ")
						check_master_pass = encode(ask_for_master_pass)
						if check_master_pass != stored_master_password:
							print("That was incorrect")
							continue
						new_id = input("Enter a new ID: ")
						with open('master_username.json', 'w') as w:
							new_master_id = json.dump(new_id, w)
					else:
						ask_for_user_pass = input("Enter your Password to continue: ")
						check_user_pass = encode(ask_for_user_pass)
						if check_user_pass != stored_password:
							print("That was incorrect")
							continue

						new_id = input("Enter a new ID: ")
						with open('username.json', 'w') as new_id_obj:
							new_id_set = json.dump(new_id, new_id_obj)
					print("Your id was saved. It is now: ")
					print(new_id)
					continue
					finish = input("Done with goals? (y/n)  ")
					if finish == str('y'):
						break
					else:
						continue


				elif account_options == str(2):
					print("Are you sure?")
					move_on = input("(y/n)")
					if move_on == str('y'):
						print("Input your old password below to continue")
						old_password = input("Enter your old password: ")
						# Encode the old password
						user_encoded_pass = encode(old_password)
						
						if user_encoded_pass != stored_master_password and user_encoded_pass != stored_password:
							print("INCORRECT")
							program_restarts = float(stored_program_data) + 1
							with open('program_data.json', 'w') as program_data_object:
								stored_program_data = json.dump(program_restarts, program_data_object)
							quit()
						elif user_encoded_pass == stored_password:
							changed_password = input("Enter a new password: ")
							
							# Encode the new password
							user_encoded_pass = encode(changed_password)
							
							with open('password.json', 'w') as password_obj:
								new_pass = json.dump(user_encoded_pass, password_obj)
							print("Your password was saved.")
							continue
						elif user_encoded_pass == stored_master_password and master_account == True:
							changed_password = input("Enter a new password: ")
							
							# Encode the new password
							user_encoded_pass = encode(changed_password)
							
							with open('master_password.json', 'w') as password_obj:
								new_pass = json.dump(user_encoded_pass, password_obj)
							print("Your password was saved.")
							continue
						else:
							print("ERROR")
							program_restarts = float(stored_program_data) + 1
							with open('program_data.json', 'w') as program_data_object:
								stored_program_data = json.dump(program_restarts, program_data_object)
							quit()
					else:
						continue
					
					
				elif account_options == str(3):
					break
		elif master_options == str(5):
			# Settings
			while True:
				print("Choose an option: ")
				print("\n" + "(1) Generate a 6 digit pin" + "\n" + "(2) Change default pin" + "\n" + "(3) Quit")
				setting_options = input()
				if setting_options == str(1):
					print("Generating....")
					time.sleep(0.4)
					print(get_auth_code(6))
				elif setting_options == str(2):
					print("Choose an option: ")
					print("(1) Random PIN, 2FA" + "\n" + "(2) Choose a satic PIN" + "\n" + "(3) Change PIN")
					pin_options = input()
					if pin_options == str(1):
						with open('typeOfAuth.json', 'w') as auth_object:
							stored_auth_type = json.dump("True", auth_object)
						print("Two-Factor Authentication has been turned on")
						break
					elif pin_options == str(2):
						with open('typeOfAuth.json', 'w') as auth_object:
							stored_auth_type = json.dump("False", auth_object)
						print("Custom Pin is now active")
						break
					elif pin_options == str(3):
						old_pin = input("Enter your old PIN to continue: ")
						if old_pin != stored_pin:
							print("FAIL")
							break
						elif old_pin == stored_pin:
							new_pin = input("Enter a new PIN:      ")
							continue_1 = input("Are you sure? (y/n)    ") 
							if continue_1 == str('y'):
								with open("pin.json", "w") as pin_object:
									stored_pin = json.dump(new_pin, pin_object)
							
				elif setting_options == str(3):
					break
		elif master_options == str(6):
			# Quit
			time.sleep(1.5)
			print("quitting")
			time.sleep(0.2)
			print("closing parsing functions...")
			time.sleep(0.1)
			print("stopping authentication...")
			time.sleep(0.1)
			print("finishing background tasks...")
			time.sleep(0.3)
			print('done')
			break
			
		else:
			print("INVALID INPUT")
			continue	
	
	
	# REGULAR ACCOUNTS
	
	elif master_account == False:
		print("Choose an option: ")
		print("\n" + "(1) Bank" + "\n" + "(2) Goals" + "\n" + "(3) Journal" + "\n" + "(4) Account" + "\n" + "(5) Login as Master" + "\n" +  "(6) Quit")
		print("\n")
		regular_options = input()
		
		# Start if-else options
		if regular_options == str(1):
			while True:
				# Bank
				print("Choose an option: ")
				print("\n" + "(1) Deposit" + "\n" + "(2) Withdraw" + "\n" + "(3) Overwrite balance" + "\n" + "(4) Quit")
				bank_options = input()
				if bank_options == str(1):
					# Deposit
					print("Great! Please enter the value you wish to depost below: ")
					deposit_ammount = input("Enter a value: ")
					total_deposit = float(stored_balance) + float(deposit_ammount)
					with open("balance.json", "w") as x:
						total_deposit_stored = json.dump(total_deposit, x)
					if valid == True:
						print("Your new total is: " + str(total_deposit))
						continue
					else:
						print("You deposited: " + str(deposit_ammount))
						continue
					# Done Deposit
					finish = input("Done with bank? (y/n)  ")
					if finish == str('y'):
						break
					else:
						continue
				elif bank_options == str(2):
					# Withdraw
					print("hmmm... okay. Enter how much you took below: ")
					withdraw_amount = input("Enter a value: ")
					total_withdraw = float(stored_balance) - float(withdraw_amount)
					with open('balance.json', 'w') as c:
						total_withdraw_stored = json.dump(total_withdraw, c)
					if valid == True:
						print("Your new total is: " + str(total_withdraw))
						continue
					else:
						print("You withdrew: " + str(deposit_ammount))
						continue
					# Done withdraw
					finish = input("Done with bank? (y/n)  ")
					if finish == str('y'):
						break
					else:
						continue
					
				elif bank_options == str(3):
					# Overwrite Balance
					print("This will overwrite your current balance.")
					proceed = input("Proceed? (y/n)  ")
					if proceed == str('y'):
						ask_for_master_pass = input("Enter the Master Password to continue: ")
						check_master_pass = encode(ask_for_master_pass)
						if check_master_pass != stored_master_password:
							print("That was incorrect")
							continue
						new_stored_balance = input("Enter a new total balance: ")
						with open("balance.json", "w") as new_balance:
							final_stored_new_balance = json.dump(new_stored_balance, new_balance)
					else:
						continue
					# Done Overwrite balance
					finish = input("Done with bank? (y/n)  ")
					if finish == str('y'):
						break
					else:
						continue
				elif bank_options == str(4):
					# Quit
					continue
				else:
					continue	
				
		elif regular_options == str(2):
			# Goals
			while True:
				print("Choose an option: ")
				print("\n" + "(1) Add a goal" + "\n" + "(2) Complete a goal" + "\n" + "(3) Quit")
				goal_options = input()
				if goal_options == str(1):
					# Add a goal
					print("Okay! Great!")
					add_goal = input("Type your goal: ")
					with open('goals.txt', 'a') as goals_file_object:
						goals_file_object.write("\n")
						goals_file_object.write(add_goal)
					finish = input("Done with goals? (y/n)  ")
					if finish == str('y'):
						break
					else:
						continue
					# end Add a goal
				elif goal_options == str(2):
					# Complete goal
					print("Awesome! Which goal did you finish? ")
					finished_goal_title = input("Enter the goal: ")
					more_goal_info = input("Enter more info about the goal! ")
					with open('goals.txt', 'a') as goals_file_object:
						goals_file_object.write("\n")
						goals_file_object.write(finished_goal_title)
						goals_file_object.write("\n")
						goals_file_object.write(more_goal_info)
					# end Complete goal
					finish = input("Done with goals? (y/n)  ")
					if finish == str('y'):
						break
					else:
						continue
				elif goal_options == str(3):
					# Quit
					break

				
		elif regular_options == str(3):
			# Journal
			while True:
				print("Choose an option: ")
				print("\n" + "(1) Add an entry" + "\n" + "(2) Quit")
				journal_options = input()
				if journal_options == str(1):
					# Start add an entry
					entry_title = input("Enter a title: ")
					entry_body = input("Enter your body text: ")
					with open('journal.txt', 'a') as journal_object:
						journal_object.write("\n")
						journal_object.write(entry_title)
						journal_object.write("\n")
						journal_object.write(entry_body)
						journal_object.write("\n")
					# End add an entry
					finish = input("Done with goals? (y/n)  ")
					if finish == str('y'):
						break
					else:
						continue
				elif journal_options == str(2):
					break
		elif regular_options == str(4):
			# Account
			while True:
				print("Choose an option: ")
				print("\n" + "(1) Change login ID" + "\n" + "(2) Change password" + "\n" + "(3) Quit")
				account_options = input()
				if account_options == str(1):
					print("OK. Please enter a new ID below: ")
					if master_account == True:
						ask_for_master_pass = input("Enter the Master Password to continue: ")
						check_master_pass = encode(ask_for_master_pass)
						if check_master_pass != stored_master_password:
							print("That was incorrect")
							continue
						new_id = input("Enter a new ID: ")
						with open('master_username.json', 'w') as w:
							new_master_id = json.dump(new_id, w)
					else:
						ask_for_user_pass = input("Enter your Password to continue: ")
						check_user_pass = encode(ask_for_user_pass)
						if check_user_pass != stored_password:
							print("That was incorrect")
							continue
						else:
							new_id = input("Enter a new ID: ")
							with open('username.json', 'w') as new_id_obj:
								new_id_set = json.dump(new_id, new_id_obj)
							print("Your id was saved. It is now: ")
							print(new_id)
							continue
					finish = input("Done with account? (y/n)  ")
					if finish == str('y'):
						break
					else:
						continue


				elif account_options == str(2):
					print("Are you sure?")
					move_on = input("(y/n)")
					if move_on == str('y'):
						print("Input your old password below to continue")
						old_password = input("Enter your old password: ")
						# Encode the old password
						user_encoded_pass = encode(old_password)
						
						if user_encoded_pass != stored_master_password and user_encoded_pass != stored_password:
							print("INCORRECT")
							program_restarts = float(stored_program_data) + 1
							with open('program_data.json', 'w') as program_data_object:
								stored_program_data = json.dump(program_restarts, program_data_object)
							quit()
						elif user_encoded_pass == stored_password:
							changed_password = input("Enter a new password: ")
							
							# Encode the new password
							user_encoded_pass = encode(changed_password)
							
							with open('password.json', 'w') as password_obj:
								new_pass = json.dump(user_encoded_pass, password_obj)
							print("Your password was saved.")
							continue
						elif user_encoded_pass == stored_master_password and master_account == True:
							changed_password = input("Enter a new password: ")
							
							# Encode the new password
							user_encoded_pass = encode(changed_password)
							
							with open('master_password.json', 'w') as password_obj:
								new_pass = json.dump(user_encoded_pass, password_obj)
							print("Your password was saved.")
							continue
						else:
							print("ERROR")
							program_restarts = float(stored_program_data) + 1
							with open('program_data.json', 'w') as program_data_object:
								stored_program_data = json.dump(program_restarts, program_data_object)
							quit()
					else:
						continue
					
					
				elif account_options == str(3):
					break	
					
		elif regular_options == str(5):
			print("Enter the master login info: ")
			change_to_master_username = input("ID: ")
			change_to_master_password = input("Password: ")
			encoded_change_to_master_password = encode(change_to_master_password)
			if encoded_change_to_master_password == stored_master_password and change_to_master_username == stored_master_username:
				# Master User Authentication
					valid = False

					store_auth_code()

					# Check the auth code 
					with open('auth.json') as auth_check:
						stored_auth_code = json.load(auth_check)
						
					print("Enter a valid key: ")
					auth = input()
					if auth != stored_auth_code:
						program_restarts = float(stored_program_data) + 1
						with open('program_data.json', 'w') as program_data_object:
							stored_program_data = json.dump(program_restarts, program_data_object)
						with open('data.txt', 'a') as data_object:
							data_object.write("\n")
							data_object.write("New user attempt on: ")
							data_object.write(time.strftime('%a %b %d'))
							data_object.write("\n")
							data_object.write("This was at: ")
							data_object.write(time.strftime('%T'))
						sys.exit("INVALID KEY")
					else:
						store_auth_code()
						print("VALID")
						# Set the valid variable to true
						valid = True
					if valid == True:
						print("Welcome, Master.")
						# If both the id and password match the master account settings, set account to activated (True)
						continue
						master_account = True
					elif valid == False:
						print("ERROR")
						quit()

				
			
		else:
			# Quit
			time.sleep(2)
			print("quitting")
			time.sleep(0.2)
			print("closing parsing functions...")
			time.sleep(0.1)
			print("stopping authentication...")
			time.sleep(0.1)
			print("finishing background tasks...")
			time.sleep(0.3)
			break