def directions():
    dir = ["Move Forward", "Move backward", "Move Left", "Move Right"]
    return dir

def menu():
    input("Please select a direction: ")
    x = directions()
    for r in x:
        print(f"{x.index(r)}:{r} ")






menu()