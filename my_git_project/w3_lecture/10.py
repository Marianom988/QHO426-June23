def sum_weights(beep,bop):
    sum = beep+bop
    return sum
def average(beep,bop):
    aver = 0.5 * (beep+bop)
    return aver

def run():
    a =int(input("What is the weight of Beep?"))
    b =int(input("What is the weight of Bop?"))
    c = input("What you would to calculate sum or average?")
    if c == "sum":
        print(f"The sum of Beep and Bop's weight is",sum_weights(a,b))
    elif c == "ave":
        print(average(a,b))

run()