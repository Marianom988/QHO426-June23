from clothingsize import Clothingsize

class Clothing:

    def __init__(self, colour="blue", material="cotton", size = Clothingsize.MEDIUM):
        self.colour = colour
        self.material = material
        self.size = size

    def __str__(self):
        return f"{self.colour} piece of clothing of size {self.size} made of {self.material}"

    def __repr__(self):
        return f"Clothing(colour ={self.colour}, material={self.material}, size={self.size})"

if __name__ == "__main__":
    tshirt = Clothing("Red", "Silk")
    jumper = Clothing(material="Polyester", size=Clothingsize.LARGE)
    print(jumper)
    print(tshirt)
    print(repr(jumper))