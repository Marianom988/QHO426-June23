from human import Human
from robot import Robot

class Planet:

    def __init__(self, n= "Planet"):
        self.name = n
        self.inhabitants = {"humans":[], "robots":[]}

    def __str__(self):
        x = [name for name in self.inhabitants["humans"]]
        y = [name for name in self.inhabitants["robots"]]
        return f"{self.name} contains : \nHumans: {x}\nRobots: {y}\n\n"


    def __repr__(self):
        return f"Planet(name ={self.name}, inhabitants={self.inhabitants})"

    def add_inhabitant(self, inh):
        if isinstance(inh, Human):
            self.inhabitants["humans"].append(inh)
        elif isinstance(inh,Robot):
            self.inhabitants["robots"].append(inh)

    # def add_robot(self,r):
    #     if isinstance(r, Robot):
    #         self.robots.append(r)
    #
    # def remove_human(self, h):
    #     if h in self.humans:
    #         self.humans.remove(h)

    def remove_inhabitant(self,inh):
        if isinstance(inh, Human):
            self.inhabitants["humans"].remove(inh)
        elif isinstance(inh, Robot):
            self.inhabitants["robots"].remove(inh)


if __name__ == "__main__":
    h1 = Human("Bob",23)
    h2 = Human("Betty",28)
    r1 = Human("Wall-E",22)
    r2 = Human("Robocop",34)
    mars = Planet()
    print(mars)
    mars.add_inhabitant(r1)
    mars.add_inhabitant(r2)
    mars.add_inhabitant(h1)
    print(mars)
    mars.add_inhabitant(h2)
    print(mars)
    mars.add_inhabitant(h2)
    print(mars)
    mars.remove_inhabitant(h1)
    mars.remove_inhabitant(r2)
    print(repr(mars))
