from person import Person, Manager
import shelve, pickle

bob = Person('Bob Smith')
sue = Person('Sue Jones', job = 'dev', pay = 100000)
tom = Manager('Tom Jones', 120000)

db = shelve.open('persondb')
for object in (bob, sue, tom):
    db[object.name] = object
db.close()    


if __name__ == "__main__":
    import shelve
    db = shelve.open('persondb')
    print(len(db))
    print(list(db.keys()))
    print(db['Tom Jones'])

    for key in db:
        print(key, '=>', db[key], db[key])

    for key in sorted(db):
        print(key, '=>', db[key])