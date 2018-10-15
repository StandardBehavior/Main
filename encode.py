# A simple program to encode passwords

import base64
import json
import hashlib


'''
Enter a password for the master account and for the regular user account
'''




quit()


x = input("Enter a string to hash:   ")
hash_object = hashlib.sha256(x.encode())
hex_dig = hash_object.hexdigest()
print("Your input: " + x)
print("Hashed form: ", hex_dig)







