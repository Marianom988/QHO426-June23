import matplotlib.pyplot as plt
with open ("temps.txt", "w") as f:
    g = {"Day ":"Temperature"}
    for i in g.items(7) :
     f.writelines(g.keys())
     f.writelines(g.values())
     print(g.keys(),g.values())
