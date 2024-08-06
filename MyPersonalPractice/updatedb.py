import shelve

db = shelve.open('persondb')

## iterate to display the objects in the database
for key in sorted(db):
    print(key, '\t =>',db[key])

sue = db['Sue Jones']  #Index by key to fetch data/object
sue.giveRaise(0.10) ## update in memoery using a class method i.e update the pay
db['Sue Jones'] = sue
db.close()