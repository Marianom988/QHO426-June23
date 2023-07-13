def display_ladder(steps):
    for i in range(0, steps):
     print("| |\n***")

def create_ladder():
    g = int(input("How many steps remain?\n"))
    steps = g
    display_ladder(steps)



create_ladder()