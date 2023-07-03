name = input("Enter your name: ")
#len() Is a function which returns the lenght of an item
#name = "piotr"
#len(name) = 5

if len(name) > 7:
    print("Your name is very long. Please provide a Nickname")
    name = input()
elif len(name) == 3:
    print("you have a very short name")
else:
    print("you have a medium name")
print(f"Welcome {name}!")