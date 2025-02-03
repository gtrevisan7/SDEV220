# Author: Gio Trevisan
# Date: 2/2/2025
# This program will ask the user to input a series of information about a car and then output all of it in a certain format

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        
    def output(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")
        
def main():
    print("Input car's information:")
    vehicle_type = "car"
    
    # Year of car input with validation
    while True:
        try:
            year = int(input("Year: "))
            if year > 0:
                break
            else:
                print("Please enter a valid positive number for the year.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the year.")
    
    # Make of car input with validation
    while True:
        make = input("Make: ").strip()
        if make.isalpha():
            break
        else:
            print("Invalid input. Please enter a valid string for the make (letters only).")
    
    # Model of car input with validation
    while True:
        model = input("Model: ").strip()
        if model.isalpha():
            break
        else:
            print("Invalid input. Please enter a valid string for the model (letters only).")
    
    # Number of doors input with validation
    while True:
        doors = input("Number of doors (2 or 4): ").strip()
        if doors in ['2', '4']:
            break
        else:
            print("Invalid input. Please enter 2 or 4 for the number of doors.")
    
    # Roof type input with validation
    while True:
        roof = input("Solid or sun roof: ").strip().lower()
        if roof in ['solid', 'sun roof']:
            break
        else:
            print("Invalid input. Please enter either 'solid' or 'sun roof' for the roof type.")
    
    car = Automobile(vehicle_type, year, make, model, doors, roof)
    
    # Formatting
    print("\n" * 2)
    
    car.output()

main()
