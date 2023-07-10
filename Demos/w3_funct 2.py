# Paratemer - data given into/injected into your function(b,h)
# default parameters - assumed if nothing is passed as argument
def t_area(b,h):
    area = 0.5*h*b


#Call to the function - make your program execute the function
total = t_area()+ t_area(5,4) + t_area(h=5)
print(f"total area is {total}")

height = float(input("Enter the height"))
base= float(input("Enter the base"))
t_area(height, base)