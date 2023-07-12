def cross_bridge(plan):
    if plan < 5:
        for i in range(1,plan+1):
            print("Crossed step.")
        print("we must keep going!")
    else:
        for f in range (1,plan+1):
            print("Crossed step.")
        print("The bridge is collapsing!")


cross_bridge(3)
cross_bridge(6)
