#initialise empty dictionary
d = {}
d2 = dict()
#initialise non empty dictionary l'elemento prima dei due punti si chiama KEY
phonebook = {"Thomas":7743434310, "Ruud":754255120, "July":78542451}
#printing individual elements
name = input("Who you gonna call?")
if name in phonebook: #quando usi if devi richiamare la KEY che sta prima dei due punti
    print(f"calling...{phonebook[name]}")
else:
    print(f"No number for {name}")
#Zipping two lists togheter into a dictionary
names = ["Marius","Nazared","Michaela"]
ages = [23, 22, 21]
people = dict(zip(names,ages))
print(people)
#Values could be anything, but KEYS must to be immutiable

#Traversing dictionaries - accessing keys/values
for thing in people:
    print(thing)

for thing in people.values():
    print(thing)
for v, k in people.items():
    print(f"Person {v} is {k} years old")