age = int(input("Enter your age: "))
ch = int(input("Enter number of children: "))

if age > 25 and ch > 2 and age <= 55: #true if all the conditions ar tue
    print("You are a parent, YAY!")
    print(f"Next year you will be {age+1}years old")
elif age >55 and ch > 0:
    print("You are slowly getting older. Hope they will support you")
elif age < 18 or ch ==0: #One or both need to be true
    print("You still have time for kids")
else:
    print("None of the conditions worked")
