while True:
	if master_account == False:
		print("(1) Deposit, (2) Withdraw, (3) Change login ID, (4) Change Password, (5) Overwrite balance, (6) Quit")
	elif master_account == True:
		print("(1) Deposit, (2) Withdraw, (3) Change login ID, (4) Change Password, (5) Overwrite balance, (6) Switch to regular account, (7) Quit")
	action = input()
	if action == str(1):
		print("Great! Please enter the value you wish to depost below: ")
		deposit_ammount = input("Enter a value: ")
		total_deposit = float(stored_balance) + float(deposit_ammount)
		with open("balance.json", "w") as x:
			total_deposit_stored = json.dump(total_deposit, x)
		if master_account == True:
			print("Your new total is: " + str(total_deposit))
			continue
		else:
			print("You deposited: " + str(deposit_ammount))
			continue
	
	elif action == str(2):
		print("hmmm... okay. Enter how much you took below: ")
		withdraw_amount = input("Enter a value: ")
		total_withdraw = float(stored_balance) - float(withdraw_amount)
		with open('balance.json', 'w') as c:
			total_withdraw_stored = json.dump(total_withdraw, c)
		if master_account == True:
			print("Your new total is: " + str(total_withdraw))
			continue
		else:
			print("You withdrew: " + str(deposit_ammount))
			continue
			
	elif action == str(3):
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
		
	elif action == str(4):
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
		
		
	
	elif action == str(5):
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
	
	elif action == str(6) and master_account == True:
		print("You will now be switched to a regular account.")
		master_account == False
		continue
	elif action == str(6) and master_account == False:
		time.sleep(2)
		print("closing")
		time.sleep(0.2)
		print("...")
		time.sleep(0.1)
		print("...")
		time.sleep(0.1)
		print("...")
		time.sleep(0.3)
		program_restarts = float(stored_program_data) + 1
		with open('program_data.json', 'w') as program_data_object:
			stored_program_data = json.dump(program_restarts, program_data_object)
		sys.exit("done")
		
	
	elif action == str('quit') or action == str(7):
		time.sleep(2)
		print("quitting")
		time.sleep(0.2)
		print("...")
		time.sleep(0.1)
		print("...")
		time.sleep(0.1)
		print("...")
		time.sleep(0.3)
		program_restarts = float(stored_program_data) + 1
		with open('program_data.json', 'w') as program_data_object:
			stored_program_data = json.dump(program_restarts, program_data_object)
		sys.exit("done")
		
	
	else:
		print("invalid input")
		time.sleep(2)
		print("Closing")
		time.sleep(0.2)
		print("...")
		time.sleep(0.1)
		print("...")
		time.sleep(0.1)
		print("...")
		time.sleep(0.3)
		program_restarts = float(stored_program_data) + 1
		with open('program_data.json', 'w') as program_data_object:
			stored_program_data = json.dump(program_restarts, program_data_object)
		sys.exit("done")
		