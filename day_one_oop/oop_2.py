class Animal:

    genus: str
    is_mammal: bool
    num_legs: int
    age: int
    sex: str

    def __init__(self, genus: str, is_mammal: bool, num_legs: int, age: int): 
        self.genus = genus
        self.is_mammal = is_mammal
        self.num_legs = num_legs
        self.age = age

    def increase_age(self) -> int: 
        self.age += 1
        return self.age
    
class Housepet(Animal):
    name: str
    breed: str

    def __init__(self, name: str)


class Dog(Housepet):
    
    def __init__(self, name: str, breed: str, age: int): 
        self.name = name
        self.breed = breed
        self.age = age 
        self.is_mammal = True
        self.num_legs = 4 

class Cat(Housepet):
    
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

kal = Dog("kal", "pit bull", 5)

housepet = Housepet("fart", "gismo")

print(isinstance(kal, Housepet))
print(isinstance(kal, Dog))

#print(issubclass(Cat, Housepet))