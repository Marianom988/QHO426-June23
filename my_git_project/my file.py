name = str(input("what is your name?\n"))
print("How old are you?")
age = int(input())
print("How tall are you?")
height = float(input())
print("How much do you weight?")
weight = float(input())
bmi = weight/(height*height)
print(f"Hi {name} you are {age} years old, your weight is {weight} kg , your height is {height} cm and your bmi is {bmi}! ")
