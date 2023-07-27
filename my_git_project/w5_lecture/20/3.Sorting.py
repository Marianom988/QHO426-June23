def observed():
    observation = []
    for i in range(5):
        f = input("Please enter an observation: ")
        observation.append(f)
    return observation

def remove_observations(observation):
    g = input("Do you wish to remove an observation? [y/n] ")
    if g == "y":
        s= input("Which observation do you wish to remove? ")
        observation.remove(s)


def run():
    whole_list = observed()
    remove_observations(whole_list)
    s = set()
    for i in whole_list:
        f = (i,whole_list.count(i))
        s.add(f)

    for f in sorted(s, reverse=True):
            print(f"{f[0]} observed {f[1]} times")


run()