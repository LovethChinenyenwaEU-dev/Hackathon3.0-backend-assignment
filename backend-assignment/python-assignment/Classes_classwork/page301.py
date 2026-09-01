# exercise 9.6

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}! We serve {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
        
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "strawberry", "chocolate", "mango"]

    def display_flavors(self):
        print(f"our flavors include: {self.restaurant_name}")

my_icecreamstand = IceCreamStand("heaven", "indian")
my_icecreamstand.display_flavors()
my_icecreamstand.describe_restaurant()


# exercise 9.7


class User:
    def __init__(self, first_name, last_name, age,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
            print(f"This is {self.first_name} {self.last_name} {self.age} {self.gender}, that works with us as a software engineer")

    def greet_user(self):
            print(f"welcome {self.first_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
         self.login_attempts = 0

class Admin(User):
     def __init__(self, first_name, last_name, age, gender):
          super().__init__(first_name, last_name, age, gender)
          self.privileges = ["can delete post", "can ban user", "can add post"]


     def show_privileges(self):
        print(f"\nAdministrator {self.first_name.title()} has the following privileges:")
        self.privileges = self.privileges
        
     
admin1 = Admin("chidimma", "rita", 40, "female")
admin1.describe_user()
admin1.show_privileges()


# exercise 9.8

class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(f"User: {self.first_name.title()} {self.last_name.title()}")

class Privileges:
     def __init__(self, privileges):
          self.privileges

     def show_privileges(self, privileges):
              print(self.privileges)

class Admin(User):
     def __init__(self, first_name, last_name, age, gender):
          super().__init__(first_name, last_name, age, gender)
          self.privileges = Privileges

new_admin = Admin("David", "charles", 31, "male")
new_admin.describe_user()
new_admin.privileges.show_privileges()

# exercise 9.9
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Prints a statement about the range this battery provides."""
        if self.battery_size == 40:
            car_range = 240
        elif self.battery_size == 65:
            car_range = 360
            print(f"This car can go approximately {car_range} miles on a full charge.")

        def upgrade_battery(self):
            if self.battery_size != 65:
                self.battery_size = 65
                print("Upgrading battery to 65 kWh...")
            else:
                print("Battery is already upgraded.")  

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model y', 2024)
print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()