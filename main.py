class Vehicle:
    count = 0
    def __init__(self, brand, model, color, wheels):
        Vehicle.count += 1
        self.sn = Vehicle.count
        self.brand = brand
        self.model = model
        self.color = color
        self.wheels = wheels
        self.mileage = 0
        return None
    
    def drive(self, distance):
        self.mileage += distance
        return None

class Bycicle(Vehicle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color, 2)
        return None
    
    @staticmethod
    def bell():
        print("🔔 BING 🔔")
        return None

class Car(Vehicle):
    def __init__(self, brand, model, color, engine, consume):
        super().__init__(brand, model, color, 4)
        self.engine = engine
        self.tank = 0
        self.fuel = None
        self.fuel_unit = None
        self.consume = consume
        match self.engine:
            case "electric":
                self.fuel = "electricity"
                self.fuel_unit = "kWh"
            case _:
                self.fuel = "gasoline"
                self.fuel_unit = "L"
        return None
    
    def drive(self, distance):
        self.tank -= distance * self.consume
        super().drive(distance)
        return None
    
    def refuel(self, amount):
        self.tank += amount
        return None

    @staticmethod
    def honk():
        print("📯 HONK 📯")
        return None
    
obj1 = Car("Tesla", "1", "white", "electric", 0.01)

obj1.refuel(100)
obj1.drive(10)
print(obj1.tank)
print(obj1.sn)

