def movements():
    path = ["Move Forward", 10, "Move backward", 5,"Move Left", 3,"Move Right",1]
    return path


def run():
    print("Moving...")
    x = movements()
    print(f"{x[0]} for {x[1]} steps\n")
    print(f"{x[2]} for {x[3]} steps\n")
    print(f"{x[4]} for {x[5]} steps\n")
    print(f"{x[6]} for {x[7]} steps\n")
    return run

run()