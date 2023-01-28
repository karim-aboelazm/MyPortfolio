from random import *
import os
user_password = input("Enter Any Password : ")
passwords = ['a','b','c','d','e','f','g','h','i','j','k','0','1','2','3','4','5','6']
pw = ''
while (pw != user_password):
    pw = ''
    for l in range(len(user_password)):
        guess_password = passwords[randint(0,17)]
        pw += str(guess_password) 
        print(pw)
        print("craking Password ... Please Wait.")
        os.system('cls')
print(f'Your Password is : {pw}')
