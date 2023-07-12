def climb_ladder(crossed,remaining):
    if crossed < remaining:
        print("Still some way to go!")
    else:
        print("We are almost there!")

climb_ladder(5,2)
climb_ladder(2,5)