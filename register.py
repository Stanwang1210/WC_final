from deepface import DeepFace
import os
from os.path import join
import cv2
import sys
from sys import exit
import glob
import time

from Person import Person
def registered_headers():
    os.system("clear")
    print("******************* Registering ************************")

def echo(string, padding=80,  for_input = False):
    padding = " " * (padding - len(string)) if padding else ""
    print(string + padding, end='\r')

def verify_name(name, registered_name):

    def pass_registration(name, registered_name):
        if name in registered_name:
            time.sleep(1)
            registered_headers()
            print("The name you entered is registered, please enter other name")
            return False
        return True

    def re_type(ans):

        if ans.capitalize()[0] == "N":
            return False
        elif ans.capitalize()[0] == "Y":
            return True
        else:
            return "Redo"

    while not pass_registration(name, registered_name):
        return False

    while True:
        registered_headers()
        ans = re_type(input(f"User name is {name}, do you want to re-type the user name (Yes/No)? ")) 
        if ans == "Redo":
            continue
        elif ans:
            registered_headers()
            return False
        elif not ans:
            registered_headers()
            return True
        else:
            print("SHIT, it wents wrong !!")
    

register_dir = "Auth"
register_file = os.path.join(register_dir, "name_list.txt")
user = Person()
name_list = open(register_file)
registered_name = []
for r in name_list:
    registered_name.append(r.replace("\n", ""))

registered_headers()
echo("Hello sir, let's start registeration !")
time.sleep(2.5)

# ****************************************************************
# Name
registered_headers()
name = input("Please type your name here : ")
while not verify_name(name = name, registered_name=registered_name):
    name = input("Please type your name here : ")

    # ans = input(f"User name is {name}, do you want to re-type the user name (Yes/No)? ")
    # # print(ans.capitalize()[0])

    # if ans.capitalize()[0] == "N":
    #     break
    # elif ans.capitalize()[0] == "Y":
    #     registered_headers()
    #     continue
    # else:
    #     name = input("Please type your name here : ")
    #     while name in registered_name:
    #         time.sleep(1)
    #         os.system("clear")
    #         print("******************* Registering ************************")
    #         print("The name you entered is registered, please enter other name")
    #         name = input("Please type your name here : ")
        
print(f"User name : {name}")
time.sleep(2.5)
exit(0)
# ****************************************************************
# Age
def is_int(value):
    try:
        int(value)
        return True
    except:
        return False
def verify_age(age):

    while not is_int(age):
        time.sleep(1)
        os.system("clear")
        print("******************* Registering ************************")
        print("Your input is not a valid age !")
        age = input("Please type your Age here : ")
    return age
os.system("clear")
print("******************* Registering ************************")
age = verify_age(input("Please type your Age here : "))
verified = False
while not verified:
    os.system("clear")
    print("******************* Registering ************************")
    ans = input(f"Your age is {age}, do you want to re-type your age (Yes/No)? ")
    # print(ans.capitalize()[0])
    if ans.capitalize()[0] == "N":
        verified = True
    elif ans.capitalize()[0] == "Y":
        os.system("clear")
        print("******************* Registering ************************")
        age = verify_age(input("Please type your Age here : "))
        
print(f"User age : {age}")
time.sleep(2.5)

# ****************************************************************
# take pictures here

pic = None

user.register(name=name, age=age, pic_path=pic)





