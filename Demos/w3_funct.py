#Definition of a function - specifying what the procedure is,and how so that it can be later called/used (maybe miltiple times)

# Paratemer - data given into/injected into your function(b,h)
# default parameters - assumed if nothing is passed as argument
def t_area(b,h):
    area = 0.5*h*b
    print(f"Area is {area}")

#Call to the function - make your program execute the function
t_area(10,20)
t_area(5,4)
height = float(input("Enter the height"))
base= float(input("Enter the base"))
t_area(height, base)