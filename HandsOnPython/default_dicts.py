from collections import defaultdict
import string
from datetime import datetime

### DEFAULTDICT
"""
Defaultdict is a subclass of the dict built in object from the collections module provides
a default value for a nonexistent key so that no KeyError is raised when trying to access 
or modify a key that does not exist yet
"""

## Example, we want to group people by department

employees = [
    ("Alice","HR"),
    ("Bob","Engineering"),
    ("Billy","IT"),
    ("Noris","Finance"),
    ("Eve","Marketing"),
    ("Diana","HR")
]

grouped = defaultdict(list)

for name, department in employees:
    grouped[department].append(name)

print(dict(grouped))


### Int use case
counts = defaultdict(int)

for letter in "banana":
    counts[letter] += 1
print(dict(counts))

help(defaultdict)


## Module: Is a single Python file, anyone can create a module apart from the built-in modules

## Packages: A collection of modules (library), most are publicly available and free

## PIP: Preferred Installer Program is a tool used to install Python Packages

## Function is code to perform a task i.e sum, len function

## Method a function that is specific to a data type or an object i.e df.head() or df.groupby()

def average(values:list, rounded:bool = True):
    """
    Calculate the average of a list of numbers.

    Args:
        values (list): a list of numerical values
        rounded (bool): boolean flag to round off the result into 2 dp. Defaults to true.

    Returns:
        average_value (float): The mean of the values in the list
    """
    ## We can use assert statement to check for types
    assert isinstance(values,list), "Only list objects allowed"
    assert isinstance(rounded,bool), "Only boolean type allowed"

    if rounded == True:
        average_value = sum(values) / len(values)
        rounded = round(average_value,2)
        return rounded
    else:
        average_value = sum(values) / len(values)
        return average_value

average.__doc__ ## dunder-doc attribute


### Arbitraty arguments
"""
Arbitrary arguments allow funtions to accept any number of arguments
Arbitrary positional arguments *args: allows functions to accept any number of positional non-keyword arguments
* means converting arguments to a single iterable (tuple)

Arbitrary keyword arguments **kwargs:  key = value
"""

def concat_strings(*args): ## single asterisk: arbitrary positional arguments tuple
    result = ""
    for arg in args:
        result += " " + arg
    print(result)
    return result
concat_strings("Home","is","best")

def concat(**kwargs): ## double asterisk: arbitrary keyword arguments dictionary
    result = ""
    for kwarg in kwargs.values():
        result += " "+kwarg
    return result

## Lambda functions
"""
Represents an anonymous function
lambda argument(s) : expresion Lambda is an exression and not a statement hence can appear in places where defs cannot appear i.e in list literals
Lambda's bosy is a single expression not a block of statements
lambda x: sum(x) / len(x)
"""
f = lambda x,y,z : x + y+ z
f(2,3,4) ## we can assign this result to another variable
xyz = f(2,3,4)

sales_price = 90.00
print((lambda: sales_price * 1.16)()) ## to get the results directly we have to add a parenthesis to call the lambda

## Lambdas can also be used to code jump tables / action tables
L = [lambda x: x **2,
     lambda x: x**3,
     lambda x : x** 4
    ]
for f in L:
    print(f(2))

## we can do the same with dictionaries
action_table = {
    "press_one": (lambda : 2 + 2),
    "press_two": (lambda: 2 * 4),
    "press_three": (lambda : 2 ** 6)
}
action_table["press_one"]()

## we can also use lambda expressions with if/else statements
lower = (lambda x,y: x if x < y else y)
lower("aa","bb")

### BUILT-IN FUNCTIONS Mapping functions over sequences: map, filter, reduce

"""
zip, 
input,
map, filter and reduce are functional programming tools which apply a function over iterables and sequences
Apply a function over an iterable i.e list object, tuple object, dictionary keys, sets
"""

## Because map expects a function to be passed, it is one place that lambdas can also appear
def inc(x):return x + 10
counters = [1,2,3,4]
counters_ = list(map(inc, counters))
counters_a = list(map((lambda x: x + 10),counters))

names = ["james","sally","carmen"]
capitals = map(lambda x: x.capitalize(),names)
print(list(capitals))

### Another built-in tool is the filter function
filtered_a = list(filter((lambda x: x < 5), list(range(-5,5))))

## Another built-in tool is the reduce function which we have to import from functools
from functools import reduce
reduced_a = reduce((lambda x,y: x + y),[1,2,3,4,5])
reduce((lambda *args: sum(args)),[90,90,90,90])


### Introduction to handling errors
"""
using try-except: will execute the except block if the try block failed
raise: will produce an error and avoids running subsequent code
"""

def compute_averages(values):
    ## Check data types
    if type(values) in [list,set,tuple]:
        average_value = sum(values)/ len(values)
        return average_value
    else:
        raise TypeError("Average() accepts a list or set, please provide a correct data type") ## provide a custom message on the raise
    


def validate_name(name):
    if type(name) != str:
        return False
    elif len(name) <= 2:
        return False
    else:
        return True
    
top_level_domains = [".org",".net",".edu",".ac",".uk",".com"]
def validate_email(email):
    valid_email = False
    username = email.split("@")[0]
    if '@' not in email:
        return valid_email
    if len(username) < 1:
        return valid_email
    for domain in top_level_domains:
        if domain in email:
            valid_email = True
    return valid_email


def validate_password(password):
    import string
    u_chars = string.ascii_uppercase
    digits = string.digits
    puncts = string.punctuation

    has_capital = False
    has_number = False
    has_puncts = False

    if len(password) < 8:
        return False
    for char in password:
        if char in u_chars:
            has_capital = True
        if char in digits:
            has_number = True
        if char in puncts:
            has_puncts = True
    if has_capital and has_number and has_puncts:
        return True
    else:
        return False



## Validate user password and return a dictionary
def validate_user(name,email, password):
    if validate_name(name) == False:
        raise ValueError("The name is not greater than two charasters or is not a string.")
    elif validate_email(email) == False:
        raise ValueError("The email address is invalid.")
    elif validate_password(password) == False:
        raise ValueError("Password is not strong enough.")
    else:
        return True


def register_user(name, email, password):
    try:
        validate_user(name, email, password)
        return {"name":name, "email": email, "password": password}
    except:
        return False
    

## Iterables, Iterators, List Comprehension, Generators
"""
Iterator: Iterating with a for and while loop on a sequences. Iterators work on iterable objects. 
Iterator is an object that has next() method which produces consecutive values.

Iterable: Is an object with a iter() method or __iter__(). These are such as lists, strings, dictionaries,
file connections.

Iterable is an object that can return an iterator, while an iterator is an object that keeps state 
and produces the next value when you call next() on it. 
 
List object is not an iterator. To make it an iterator, we apply the iter method. 
In this regard, the list
object is an iterable, because the iter() methid can be applied to it to return an iterator.
"""


flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen'] ## an iterable object
for f in flash: print(f)

flashes = iter(flash) ## converted to an iterator

print(next(flashes)) ## now we can use the next() method on it to get the next item in the sequence
print(next(flashes))
print(next(flashes))


## Enumerate and zip functions
## Enumerate keeps the counter index within an iterator
for idx, value in enumerate(flash, start = 1): ## we can also pass a start argument here
    print(idx, value)


## zip accepts an arbitrary number of iterable object(s) and returns an iterator of tuples
