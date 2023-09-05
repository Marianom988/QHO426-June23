from inhabitant import Alien

class Alien(Inhabitant):

    def __init__(self, n="Alien"):
        super().__init__(n)
        self.technology = []