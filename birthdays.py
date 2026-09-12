from collections import defaultdict

def run_birthdays(birthdays):
    while True:
        print("Enter a name: (blank to quit)")
        name = input()
        if name == "":
            break
        if name in birthdays: ## check if the key provided exists in the dictionary's keys
            print(f"{birthdays[name]} is the birthday of {name}") ## get the associated value
        else:
            print(f"I do not have a birthday info for {name}")
            print("What is their birthday ?")
            bday = input()
            birthdays[name] = bday ## if the name does not exist, you can add it to the dictionary and assign a value to the key using the assignment operator
            print("Birthday updated to the database")

## run as a top level file
if __name__ == "__main__":
    birthdays = {
    "Alice":"April 1",
    "Alex": "September 15",
    "Bob": "December 12",
    "Carol" : "March 4"
    }
    run_birthdays(birthdays)

