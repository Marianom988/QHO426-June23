def directions():
    dir = ["Move Forward", "Move backward", "Move Left", "Move Right"]
    return dir

def menu():
    print("Please select a direction: ")
    x = directions()
    for r in x:
        print(f"{x.index(r)}:{r} ")
    b = int(input())
    f = x[b]
    return f


def run():
    route = []
    print("Working escape route...\n")
    for d in range(5):
        route.append(menu())
    print(route)


run()