def dimensions():
    w= float(input("enter width of the room"))
    l = float(input("enter lenght of the room"))
    return l*w

def r_name():
    return input("enter room name")

def price(name,area):
    if name.lower() == "bathroom":
        return 15*area
    elif name.lower()  == "bedroom":
        return 8*area
    else:
        return 10*area

def run():
    t_price = 0
    num = int(input("How many rooms to clean? "))
    for i in range (num):
        room = r_name()
        area = dimensions()
        p = price(room, area)
        t_price += p
    print(f"The total price is £{t_price}")
run()