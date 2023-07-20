def directions():
    direction = ["Move forward", "Move backward", "Turn left", "Turn right"]
    return direction


def run():
    x = directions()
    for i in range(len(x)):
        print(i)
run()
