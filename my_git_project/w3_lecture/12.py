def play_guess_the_number():
    import random as rdn
    f = int(input("Enter the minimum value: "))
    h = int(input("Enter the maximum value: "))
    s = (rdn.randrange(f,h))
    print(f"I am thinking a number between {f} e {h}. Can you guess what is? ")
    for tol in range(1,6):
        k =int(input())
        print(f"try number {tol}")
        if k < s :
         print("Your guess is too low!\nTry again")
        elif k >s:\
        print("Your guess is too high!\nTry again")
        elif k == s:\
        print("Congratulations you guess my number!")

play_guess_the_number()

