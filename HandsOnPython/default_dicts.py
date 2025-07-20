from collections import defaultdict

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