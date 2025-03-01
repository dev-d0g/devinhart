"""
The four principles of object oriented programming (OOP):

1. Encapsulation
    * encapsulate data & functions related to said data within "objects"
2. Inheritance
    * allows classes to inherit properties (data) and behaviors (functions) from parent classes 
    * creates a hierarchy of classes which promotes code reuse (addition of housepet to this file was an example of reuse)

3. Polymorphism
    

4. Abstraction
    * when multiple classes share some of the same properties/functionality, you can abstract these things into a shared class from which both "subclasses" inherit
"""

class Animal:
    genus: str
    is_mammal: bool
    num_legs: int
    age: int
    sex: str

    # Example 1 of Animal constructor (commented out because python only allows one __init__ function per class)
    # constructor signatures in Python will look like def __init__(self, ...):
    # def __init__(self): #constructor function
    #     self.genus = ""
    #     self.is_mammal = False
    #     self.num_legs = 0

    # Example 2 of Animal constructor
    def __init__(self, genus: str, is_mammal: bool, num_legs: int, age: int): 
        self.genus = genus
        self.is_mammal = is_mammal
        self.num_legs = num_legs
        self.age = age


    """Increases the age of the animal by one, and returns the age."""
    def increase_age(self) -> int: #do not have to define return type (nor the function parameter types)
        self.age += 1
        return self.age



#### Learnings here
# OOP is related to inheritance, what we see here. We're defining a new class called Dog which "inherits"
# the features of an animal while also having features (variables/data) of its own that are specific to
# its needs
class Dog(Animal):
    #self referes to these members
    name: str
    breed: str
    
    # the variables you pass into a function are called "parameters" when you define the signature
    # so __init__ has two string parameters "name" & "breed"
    # but when you actually call the function and pass in real values they're known as "arguments"
    # so if we say Dog("kal", "pitbull") now we have passed in string arguments "kal" & "pitbull"
    def __init__(self, name: str, breed: str, age: int): 
        self.name = name
        self.breed = breed
        self.age = age 
        self.is_mammal = True
        self.num_legs = 4 


# did you cook your headset


class Cat(Animal):
    name: str
    breed: str
    skiddish: bool
    menace: bool

    def __init__(self, dumb_name: str, dumb_breed: str, dumb_skiddish: bool, dumb_menace: bool, age: int, dumb_sex: str):
        self.name = dumb_name
        self.breed = dumb_breed
        self.skiddish = dumb_skiddish
        self.menace = dumb_menace
        self.num_legs = 4
        self.age = age 
        self.genus = "felis"
        self.is_mammal = True
        self.sex = dumb_sex

pip = Cat("pip", "maine coon", True, False, 1, "male")


tipsy = Cat("tipsy", "maine coon", True, False, 1, "female")

my_animal = Animal("homo sapien", True, 2, 22)

kal = Dog("kal", "pit bull", 5)

bindy = Dog("bindy", "golden", 1)

print(pip.sex)
