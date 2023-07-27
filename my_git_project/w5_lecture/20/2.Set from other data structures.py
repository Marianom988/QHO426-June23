def observed():
    observations = []
    while True:
        g = str(input("Please enter an observation: "))
        observations.append(g)
        if len(observations) == 7:
            break
    return observations



def run():
    print("Counting observations...")
    x = observed()
    s = set()
    for i in x:
        data = (i, x.count(i))
        s.add(data)

    for data in s:
        print(f"{data[0]} Observed {data[1]} times")





run()

