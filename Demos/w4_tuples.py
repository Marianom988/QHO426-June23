#Declare a tuple
x = ("Mariano", 34, True)
y = tuple(["Gary",23, False])
#Print tuples
print(x)
print(y)
print(x[2])
print(y[1])
print(y[0:2])
#Cannot change individual items (immutability)
#x[1] += 1 non funziona perche' non pupoi cambiare un tuple

#Concatenate tuples
z= x + y
print(z)
print(x)
print(y)

#Use min and max function on tuples

t = (74, 35, 1, 83, 65, 62)
print(max(t))
print(min(t))

#Fixing errors
print(x)
l1 = list(x)
l1[2] = False
x= tuple(l1)
print(x)