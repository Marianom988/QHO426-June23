def ascii(art):
    g = f"####\n#{art}#\n####"
    return g


def lowe(low):
    p = str.lower(low)
    return p


def upp(upper):
    s = str.upper(upper)
    return s


def mirror(mir):
    s = mir [::-1]
    print(f"{mir}|",end="")
    return s


def repe(rep):
    d = int(input("How may times do you want me to repeat it?\n"))
    for i in range(0,1,2):
        for g in range(0,d,2):
            print(rep)
            print(str.upper(rep))

        return i




def program():
    h = int(input("chose one option:\n1. Display in a box.\n2. Display Lower-case.\n3. Display Upper-case.\n4. Display Mirrored.\n5. Repeat.\n"))
    l = input("Please enter a word:\n")
    if h == 1:
        print(ascii(l))
    elif h == 2:\
            print(lowe(l))
    elif h == 3:\
            print(upp(l))
    elif h == 4:\
            print(mirror(l))
    elif h == 5:\
            print(repe(l))

program()