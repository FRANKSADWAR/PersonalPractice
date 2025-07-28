from collections import defaultdict
import string
from datetime import datetime
import pandas as pd

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
zip(flash)


#### unzip the contents of a zip using * 
# Create a zip object from mutants and powers: z1
mutants = ['a','b','c']
powers = [10,11,12]

z1 = zip(mutants,powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)


### we can now use the 
def count_entries(csv_file,c_size,colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize = c_size):
        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1
    # Return counts_dict
    return counts_dict

# Call count_entries(): result_counts
result_counts = count_entries('tweets.csv',10,'lang')

# Print result_counts
print(result_counts)



"""
LIST COMPREHENSIONS
"""
list1 = [90,89,67]
list2 = [12,34,56]

# list comprehension
y = [x+ 19 for x in list1]

## use with conditional stament
[x for x in range(5) if x % 2 ==0 ]

## when we want a result for the false condition as well, we start with the conditions first
[num**2 if num % 2 ==0 else 0 for num in range(10)]

## use nested for loops in a list comprehension
pairs = [(num1, num2) for num1 in range(0,2) for num2 in range(10,12)]
print(pairs)

list(map((lambda x: x + 2),list1))

"""
DICTIONARY COMPREHENSIONS

Dictionaries can also be created using dictionaty comprehensions
"""

d = dict(zip(list1,list2))
d2 = {k:v for (k,v) in zip(list1,list2)}

{c.upper():c for c in ['Homer','Lab']}

"""
GENERATORS

Generators support what is called lazy evaluation or loading.

Generator functions:  are coded using the similar construct as the def function but uses yield keyword to return results
Generator expressions: are similar to list comprehensions but results are wrappedin a parentheses ()
The advantage of generators is that results do not have to be loaded into memory.
This can save memory when a function's results are large or require a lot of computation to produce each value
"""

def buildsquares(n):
    res = []
    for i in range(n):
        res.append(i**2)
    yield res   ## use yield instead of return, which will produce results using the .next method



# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
# Create a generator object: lengths
lengths = (len(person) for person in lannister)  ## return a generator object instead of list
# Iterate over and print the values in lengths
for value in lengths:
    print(value)



# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield (len(person))

# Print the values generated by get_lengths()
for value in get_lengths(lannister):
    print(value)


row_lists = [['Arab World',
  'ARB',
  'Adolescent fertility rate (births per 1,000 women ages 15-19)',
  'SP.ADO.TFRT',
  '1960',
  '133.56090740552298'],
 ['Arab World',
  'ARB',
  'Age dependency ratio (% of working-age population)',
  'SP.POP.DPND',
  '1960',
  '87.7976011532547'],
 ['Arab World',
  'ARB',
  'Age dependency ratio, old (% of working-age population)',
  'SP.POP.DPND.OL',
  '1960',
  '6.634579191565161'],
 ['Arab World',
  'ARB',
  'Age dependency ratio, young (% of working-age population)',
  'SP.POP.DPND.YG',
  '1960',
  '81.02332950839141'],
 ['Arab World',
  'ARB',
  'Arms exports (SIPRI trend indicator values)',
  'MS.MIL.XPRT.KD',
  '1960',
  '3000000.0'],
 ['Arab World',
  'ARB',
  'Arms imports (SIPRI trend indicator values)',
  'MS.MIL.MPRT.KD',
  '1960',
  '538000000.0'],
 ['Arab World',
  'ARB',
  'Birth rate, crude (per 1,000 people)',
  'SP.DYN.CBRT.IN',
  '1960',
  '47.697888095096395'],
 ['Arab World',
  'ARB',
  'CO2 emissions (kt)',
  'EN.ATM.CO2E.KT',
  '1960',
  '59563.9892169935'],
 ['Arab World',
  'ARB',
  'CO2 emissions (metric tons per capita)',
  'EN.ATM.CO2E.PC',
  '1960',
  '0.6439635478877049'],
 ['Arab World',
  'ARB',
  'CO2 emissions from gaseous fuel consumption (% of total)',
  'EN.ATM.CO2E.GF.ZS',
  '1960',
  '5.041291753975099'],
 ['Arab World',
  'ARB',
  'CO2 emissions from liquid fuel consumption (% of total)',
  'EN.ATM.CO2E.LF.ZS',
  '1960',
  '84.8514729446567'],
 ['Arab World',
  'ARB',
  'CO2 emissions from liquid fuel consumption (kt)',
  'EN.ATM.CO2E.LF.KT',
  '1960',
  '49541.707291032304'],
 ['Arab World',
  'ARB',
  'CO2 emissions from solid fuel consumption (% of total)',
  'EN.ATM.CO2E.SF.ZS',
  '1960',
  '4.72698138789597'],
 ['Arab World',
  'ARB',
  'Death rate, crude (per 1,000 people)',
  'SP.DYN.CDRT.IN',
  '1960',
  '19.7544519237187'],
 ['Arab World',
  'ARB',
  'Fertility rate, total (births per woman)',
  'SP.DYN.TFRT.IN',
  '1960',
  '6.92402738655897'],
 ['Arab World',
  'ARB',
  'Fixed telephone subscriptions',
  'IT.MLT.MAIN',
  '1960',
  '406833.0'],
 ['Arab World',
  'ARB',
  'Fixed telephone subscriptions (per 100 people)',
  'IT.MLT.MAIN.P2',
  '1960',
  '0.6167005703199'],
 ['Arab World',
  'ARB',
  'Hospital beds (per 1,000 people)',
  'SH.MED.BEDS.ZS',
  '1960',
  '1.9296220724398703'],
 ['Arab World',
  'ARB',
  'International migrant stock (% of population)',
  'SM.POP.TOTL.ZS',
  '1960',
  '2.9906371279862403'],
 ['Arab World',
  'ARB',
  'International migrant stock, total',
  'SM.POP.TOTL',
  '1960',
  '3324685.0']]

# Define lists2dict()
def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""

    # Zip lists: zipped_lists
    zipped_lists = zip(list1, list2)

    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)

    # Return the dictionary
    return rs_dict
    



# Print the first two lists in row_lists
print(row_lists[0])
print(row_lists[1])

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Print the first two dictionaries in list_of_dicts
print(list_of_dicts[0])
print(list_of_dicts[1])