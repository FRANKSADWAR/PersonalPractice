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