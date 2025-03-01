from enum import Enum

# Briefly: Make is an enum or enumeration of values. It's a finite thing, it doesn't require functiality, etc
class Make(Enum):
    HONDA = "Honda"
    FORD = "Ford"
    TOYOTA = "Toyota"
    RAM = "Ram"

class Car:
    make : Make
    model : str
    year : int

    def __init__(self, _make: Make, _model: str, _year: int):
        self.make = _make
        self.model = _model
        self.year = _year

    def is_piece_of_shit(self) -> bool:
        return self.make == Make.FORD
    
    def is_worth_something(self) -> bool:
        return self.make != Make.RAM

class Truck(Car):
    bed_length: int
    is_lifted: bool
    
    def __init__(self, _bed_length: int, _is_lifted: bool, _make: Make, _model: str, _year: int):
        self.bed_length = _bed_length
        self.is_lifted = _is_lifted
        self.make = _make
        self.model = _model
        self.year = _year

    def is_piece_of_shit(self) -> bool:
        return self.bed_length < 8


class Sedan(Car):
    diesel: bool

    def __init__(self, _diesel: bool, _make: Make):
        self.diesel = _diesel
        self.make = _make

    # def is_piece_of_shit(self):
    #     return False


my_dads_truck = Truck(7, False, Make.RAM, "1500", 2021)
# print(f"Is a piece of shit? {my_dads_truck.is_piece_of_shit()}")

# Polymorphism allows objects of different classes to be treated as if they are of the same class
# below, sedan is of class "Sedan", truck is of class "Truck"
# both however, can call "is_worth_something" and "is_piece_of_shit" because they inherit from the same parent class
# their ability to call these functions is "Polymorphism"

# Nice example: https://stackoverflow.com/a/3110318

sedan = Sedan(False, Make.HONDA)
truck = Truck(1, False, Make.FORD, "F150", 2011)

cars: list[Car] = [Sedan(False, Make.HONDA), Sedan(False, Make.FORD), Truck(1, False, Make.FORD, "F150", 2011), Truck(1, False, Make.RAM, "1500", 2001)]

# print("Without Sedan is_piece_of_shit")
# for car in cars:
#     print(f"Car make {car.make}. Is car piece of shit: {car.is_piece_of_shit()}")

# ---------------------------------------------------------------------------------------------
class A:
    a = 'a'

    # def get_value(self):
    #     return self.a

class B(A):
    b = 'b'

    def get_value(self):
        return 'b'
        
class C(B):
    c = 'c'

    # def get_value(self):
    #     return self.c

class D(C):
    d = 'd'

    # no get_value() defined
    # so it looks at its parent. if not there, looks at that parent's parent. recursive.
    # if never found, error thrown / program halts
    

# d = D()
# print(d.get_value())

a = A()
print(a.get_value())