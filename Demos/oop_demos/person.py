#The class Person which is a  blue print for my objects to store information about people
class Person:

    #CLASS Attribute - attribute/feature accessible to every project
    MAX_W = 150

    #Static method - Utility function that does not require an object to work
    def is_mature(age):
        if age >= 18:
            return "person is mature"
        else:
            return "Person is immature"

     #Initialiser/Constructor - function automatically called when and object
     # is instantiated (magic method )
     #initialiser of ANY class has the name
     #self is a reference to an object instantiated
     #DUNDER - Double Underscore
    def __init__(self, name = "Jhon", age = 0, job= "None", w= MAX_W):
         self.name = name
         self.age = age
         self.job = job
         if w > Person.MAX_W:
             self.weight = Person.MAX_W
         else:
             self.weight = w

    # Magic method str provides "informal" representation of an object via string
    #Automatically invoked when passing object to print
    def __str__(self):
        return f"{self.name} is {self.age} years old. They work as {self.job} and weight {self.weight}"
         #Instance Attributes (features of an object)

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age},job={sel.age}, weight={self.weight}"

     #instance method - a method that applies to a specific instance of the class
     #Method - function attached to a specific data type (class)
    def eat(self, food,w):
         print(f"{self.name} has eaten {food}")
         self.weight += w
         print(f"{self.name} now weights {self.weight} kg")

    def exercise(self, burned):
        self.weight -= burned
        print(f"{self.name} now weights {self.weight} kg")



#Object instantiation - creating new instance from the class
if __name__ == "__main__":
    print(Person.is_mature(19))
    p1 = Person("Mariano", 55, "tutor" )
    p2 = Person("Carlo", 25, "cleaner" )
    print(Person.is_mature(p2.age))
    print(p1)
    p1.eat("ice cream", 0.3)
    p2.eat("goulash", 1)
    p1.exercise(0.1)
    p1.exercise(0.45)
    p2.exercise(0.2)
    print(p1)
    print(p2)
