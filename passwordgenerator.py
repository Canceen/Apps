import random
from variables import *

while True:
    print()
    print("*** :3 MEOW :3 ***")
    print("Welcome to the random password generator!")
    print()
    print("By defult password are only created in lower case")
    print("To exit, type 0 and hit return at any stage.")
    print("Do you want to include upper case letters? (y/n)")    
    print()
    user_input = input("Enter an option: ")
    
    if user_input in main_menu_options:
        break
    
    else:
        print()
        print("Error, please use (y) or (n) or (x) to exit")
                
if user_input == "x":
    exit
elif user_input == "y":
     upper = True
elif user_input == "n":
     upper = False     
    
while True:
    print()
    print("Thank you, do you want to include numbers? (y/n)")
    print()
    user_input = input("Enter an option: ")
    
    if user_input in main_menu_options:
        break    
    else:
        print()
        print("Error, please use (y) or (n) or (x) to exit")
        
if user_input == "x":
    exit
elif user_input == "y":
    nums = True
elif user_input == "n":
    nums = False
    
while True:
    print()
    print("Thank you, do you want to include special characters? (y/n)")
    user_input = input("Enter an option: ")
    
    if user_input in main_menu_options:
        break    
    else:
        print()
        print("Error, please use (y) or (n) or (x) to exit")
        
if user_input == "x":
    exit
elif user_input == "y":
    syms = True
elif user_input == "n":
    syms = False   
    
while True:
    print()
    print("How long would you like the password to be? " + num_range_text)

    user_input = int(input("Enter password length: "))

    if user_input in length_scale_options:
        break
    else:
        print()
        print("Error, type a number between " + num_range_text)
        
if user_input in length_scale_options:
    length = int(user_input)
    
else:
    print()
    print("Error please enter a number between " +num_range_text)
 
file = open('passwordproject.txt', "w")
lower = True
upercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
special_characters = "!$%^&*#@"

all = ""
if upper:
    all += upercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += special_characters
    
for x in range(numberofpw):
    password = "".join(random.sample(all, length))
    print()
    print("Your generated password:")
    print()
    print(password)

while True:
    print()
    print("x = Exit without saving")
    print("y = Save & Exit")
    user_input = input("Do you want to save this password to a text file? ")
    if user_input in exit_menu_options:
        break
    else:
        print("Error, choose (x) or (y)! ")
if user_input == "x":
    file.close
    exit
if user_input == "y":
    file.write(password)
    file.close
    exit