import base64
import json
import time
import sys
import random



# Options
# 1. Bank
# 2. Goals
# 3. Journal
# 4. Account
# 5. Settings

master_account = True


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
							sys.exit()
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
							sys.exit()
					else:
						continue
					
					
				elif account_options == str(3):
					break
		elif master_options == str(5):
			# Settings
			while True:
				print("Choose an option: ")
				print("\n" + "(1) Generate a 6 digit pin" + "\n" + "(2) Quit")
				setting_options = input()
				if setting_options == str(1):
					print("Generating....")
					time.sleep(0.4)
					print("done")
					print(get_auth_code(6))
				elif setting_options == str(2):
					break
		elif master_options == str(6):
			# Quit
			time.sleep(2)
			print("quitting")
			time.sleep(0.2)
			print("...")
			time.sleep(0.1)
			print("...")
			time.sleep(0.1)
			print("...")
			time.sleep(0.3)
			sys.exit("done")
			
		else:
			print("INVALID INPUT")
			continue	
	
	
	elif master_account == False:
		print("Choose an option: ")
		print("\n" + "(1) Bank" + "\n" + "(2) Goals" + "\n" + "(3) Journal" + "\n" + "(4) Account" + "\n" + "(5) Quit")
		print("\n")
		regular_options = input()
		
		# Start if-else options
		if master_options == str(1):
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
							sys.exit()
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
							sys.exit()
					else:
						continue
					
					
				elif account_options == str(3):
					break	
	else:
		# Quit
		time.sleep(2)
		print("quitting")
		time.sleep(0.2)
		print("...")
		time.sleep(0.1)
		print("...")
		time.sleep(0.1)
		print("...")
		time.sleep(0.3)
		sys.exit("done")
		
		
		
		
		
		