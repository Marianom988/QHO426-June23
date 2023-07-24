#initialite empty sets
s = set()
#initialise non empty set using curly brackets. empty breckets create dictionary
s1 = {1,2,3,4}
col = {"blue","green","red","yellow","black"}
print(col)
#add items to the set
col.add("purple")
col.add("orange")
print(col)
#adding more than 1 items at once
col = col.union({"white","brown","crimson", "magenta"})
print(col)
#remove
if "yellow" in col:
   col.remove("yellow")
print(col)
#heterogeneous
col.add(99)
col.add(False)
print(col)
print("-"*20)
c= {"brown","turqoise", "pink","cyan","green"}
#Union join 2 sets togheter, not keeping duplicate
c2 = col.union(c)
print(f"col is {col}")
print(f"c is {c}")
print(f"c2 is {c2}")
#intersection (items in common in 2 sets)
c3 = col.intersection(c)
print(f"c3 is {c3}")

#Difference - keep elements of one set, that are not part of the other
c4 = c.difference(col)
c5 = col.difference(c)
print(f"c4 is {c4}")
print(f"c5 is {c5}")