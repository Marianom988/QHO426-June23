i = input("where should I look?")
if i == "in the bedroom":
    print("Where in the bedroom should I look?")
    g = input()
    if g == "under the bed":
        print("Found some shoes but no battery")
    else: print("found some mess but no battery")
elif i == "in the bathroom":
    print("Where in the bathroom should I look?")
    g = input()
    if g == "in the bathtub":
        print("Found a rubber duck but no battery.")
    else: print("Found a wet surface but no battery")
elif i == "in the lab":
    print("where in the lab should I look")
    h = input()
    if h == "on the table":
            print("Yes! I found my battery!")
    else: print("found some tools but no battery")
else: print("I don't know where that is but I will keep looking.")

