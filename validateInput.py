from __future__ import print_function

while True:
    print('Enter your age')
    age = input()
    if age.isdecimal():
        break ## Break out of the loop if the condition is met
    print('Please enter a number for your age')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break   ## Break out of the loop if the condition is met
    print('Passwords can only have letters and numbers')
