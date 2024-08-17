from abc import ABC, abstractmethod

def kaboom(x,y):
    print(x+y)

if __name__ == "__main__":
    try:
        kaboom([0,1,2],"Spam")
    except TypeError:
        print("Type must be the same")
    print("--- Resuming here")

"""
When the exception occurs in the function kaboom, control jumps to the try statement's exept clause, which promts a print message.

"""

try:
    print('test')
finally:
    print('Always run this')