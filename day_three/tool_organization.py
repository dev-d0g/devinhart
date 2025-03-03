from enum import Enum

class Brand(Enum):
    MILWAUKEE = "Milwaukee"
    DEWALT = "DeWalt"
    BOSCH = "Bosch"
    CRAFTSMAN = "Craftsman"
    HARBOR_FREIGHT = "Harbor_Freight"

class Finish(Enum):
    CHROME = "Chrome"
    BLACK_OXIDE = "Black Oxide"
    NA = "N/A"

class Drive(Enum):
    QUARTER = "1/4-inch"
    THREE_EIGHTHS = "3/8-inch"
    HALF = "1/2-inch"
    OTHER = "Other"

class Application(Enum):
    AUTOMOTIVE = "Automotive"
    WOODWORKING = "Woodworking"
    ELECTRONICS = "Electronics"

class Power_Source(Enum):
    Corded = "AC - Corded"
    Battery = "DC - Battery"

class Tool:
    brand : Brand
    name : str
    model_number : str
    application : Application
    price : float

    def __init__(self, _brand: Brand, _application: Application, _name : str, _model_number: str, _price: float):
        self.brand = _brand
        self.application = _application
        self.name = _name
        self.model_number = _model_number
        self.price = _price

class Handtool(Tool):
    type = "Handtool"
    finish : Finish
    drive : Drive
    grip_type : str

    def __init__(self, _brand: Brand, _application: Application, _name : str, _model_number: str, _price: float, _finish: Finish, _drive: Drive, _grip_type : str):
        super().__init__(_brand, _application, _name, _model_number, _price)
        self.finish = _finish
        self.drive = _drive
        self.grip_type = _grip_type

class Powertool(Tool):
    type = "Powertool"
    power_source : Power_Source
    voltage : int

    def __init__(self, _brand: Brand, _application: Application,  _name : str, _model_number: str, _price: float, _power_source: Power_Source, _voltage: int):
        super().__init__(_brand, _application, _name, _model_number, _price)
        self.price = _price
        self.power_source = _power_source
        self.voltage = _voltage

tools : list[Tool] = [                    
    Powertool(Brand.MILWAUKEE, Application.AUTOMOTIVE, "1/2-inch impact wrench", "ABC123", 250, Power_Source.Battery, 18),
    Powertool(Brand.BOSCH, Application.WOODWORKING, "Orbital Sander", "DEF456", 120, Power_Source.Corded, 120),
    Handtool(Brand.HARBOR_FREIGHT, Application.AUTOMOTIVE, "3/8-inch ratchet", "GHS38223", 10, Finish.CHROME, Drive.THREE_EIGHTHS, "Metal"),
    ]

print("Tool names:\n")
for tool in tools:
    print(f"{tool.name}\n")








