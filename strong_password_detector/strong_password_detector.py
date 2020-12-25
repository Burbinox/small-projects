# this program check if password is strong enough using regex library 
# made by Hubert Grobelny

import re

while True:
    password = input("Input your password: ")
    if len(password) < 4:
        print("Your password is too short, try again:")
    elif not re.search("[a-z]", password):
        print("password don't have a-z")
        print("password weak, not strong enough")
    elif not re.search("[0-9]", password):
        print("password don't have 0-9")
        print("password weak, not strong enough")
    elif not re.search("[A-Z]", password):
        print("password don't have A-Z")
        print("password average, not strong enough")
    elif not re.search(r'[^A-Za-z0-9]', password):
        print("password don't have special charakters")
        print("password average, not strong enough")
    else:
        print("This is strong enough password")
        break
