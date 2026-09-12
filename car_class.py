class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model =model
        self.year = year
        self.odometer_reading = 0
    def descriptive_name(self):
        long_name = print(f"{self.make}  {self.model} {self.year}")
        return long_name

    def read_odometer(self):
        print(f"The odometer reading is {self.odometer_reading}")

    def update_odometer(self,millage):
        if millage >= self.odometer_reading:

            self.odometer_reading = millage

        else:   
            print("You can not roll back millage")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)

        self.battery_size =40
    def describe_battery(self):
        print(f"{self.battery_size} watts is the current size of te battery")


new_ccar= Car("Audi","a4",2026)

print(new_ccar.descriptive_name())
# new_ccar.odometer_reading = 30
my_leaf = ElectricCar("nissin","leaf",2024)

print(my_leaf.descriptive_name())
my_leaf.describe_battery()

new_ccar.update_odometer(300)
new_ccar.update_odometer(30)
new_ccar.read_odometer()