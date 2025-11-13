# die Klasse Vehicle stellt Eigenschaften und Methoden bereit, die alle Fahrzeuge mit einander teilen
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
        # da das wiederholt angesprochen wurde: dieses return ist für den Code völlig egal.
        # wenn man nach einem return eine neue Zeile einfügt, rückt VSC einen automatisch ein,
        # damit man direkt mit der def einer neuen Funktion anfangen kann.
        # Dadurch ist es später einfacher, neue Methoden einzufügen, ohne sich lange mit der Einrückung zu befassen.
        return None

    # jedes Fahrzeug kann fahren, daher ist die Methode hier sinnvoll
    def drive(self, distance):
        self.mileage += distance
        return None

class Bycicle(Vehicle):
    def __init__(self, brand, model, color):
        # mit super() kann man eine gleichnamige Methode von der Eltern-Klasse ansprechen.
        # manchmal kennt man Werte bereits, wie die Anzahl der Räder eines Fahrrads
        # diese kann man dann im super()-Aufruf angeben und muss sie nicht mehr in der init der Child-Klasse abfragen
        super().__init__(brand, model, color, 2)
        return None

    # eine @staticmethod braucht kein self. Sie ist sinnvoll für Methoden, die nicht mit den Eigenschaften des Objekts interagieren müssen
    @staticmethod
    def bell():
        print("🔔 BING 🔔")
        return None

# beliebig viele Klassen können von der selben Eltern-Klasse erben und eigene Methoden definieren
class Car(Vehicle):
    def __init__(self, brand, model, color, engine, consume):
        super().__init__(brand, model, color, 4)
        self.engine = engine
        self.tank = 0.0
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

    # man kann Methoden von Eltern-Klassen überschreiben. Wenn man das nicht macht, wird einfach die Version der Eltern-Klasse verwendet
    def drive(self, distance):
        self.tank -= distance * self.consume
        # auch hier funktioniert super().
        # So kann man Dinge wie das Treibstoff-Management hinzufügen und trotzdem die drive-Methode der Eltern-Klasse nutzen
        super().drive(distance)
        return None

    def refuel(self, amount):
        self.tank += amount
        return None

    @staticmethod
    def honk():
        print("📯 HONK 📯")
        return None

# Es ist auch möglich, von mehreren Klassen gleichzeitig zu erben. Das ist vermutlich zu kompliziert für diesen Punkt der Schulung.
# Beim erben von mehreren Klassen ist die Reihenfolge wichtig!
# am besten sortiert man sie aufsteigend nach Anzahl der benötigten Parameter
class Mofa(Bycicle, Car):
    def __init__(self, brand, model, color, consume):
        # In diesem Fall muss explizit gesagt werden, wessen __init__ verwendet werden soll.
        # am besten nimmt man die __init__ der letzten Klasse, von der man erbt
        Car.__init__(self, brand, model, color, "combustion", consume)
        # nach dem __init__ muss man vielleicht Werte überschreiben
        # in diesem Fall hat Car.__init__ die Räder-Zahl auf 4 gesetzt, aber eine Mofa hat nur zwei Räder.
        self.wheels = 2
        return None

    @staticmethod
    def honk():
        super().bell()
        return None

obj1 = Car("Tesla", "1", "white", "electric", 0.01)

obj1.refuel(100)
obj1.drive(10)
print(obj1.tank)
print(obj1.sn)

mofa1 = Mofa("selfmade", "1", "green", 0.1)
mofa1.refuel(42)
print(f"Rad-Zahl: {mofa1.wheels}")
print(f"Tank-Füllstand: {mofa1.tank}")
mofa1.drive(100)
mofa1.bell()
print(f"nach 100 km sind noch {mofa1.tank}{mofa1.fuel_unit} im Tank.")
