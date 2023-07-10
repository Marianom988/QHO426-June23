import random

secret_n = random.randint(1,20)
print("Welcome to my guess game! i am thinking a number between 1 and 20")

for attempt in range(1,6):
    print(f"attempt nr {attempt}")
    guess = int(input("Take a guess"))
    if guess == secret_n:
        print("Congrats you have guessed correctly")
        break
    elif guess > secret_n:
        print("too high!")
    else:
        print("too low!")
if guess != secret_n:
    print(f"game over! My number was {secret_n}")