# execise 9.4
class Restaurant:
    """Initializing restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print (f"Welcome to {self.restaurant_name}, there is varity of {self.cuisine_type} food")

    def open_restaurant(self):
        print(f"{self.restaurant_name}, is now open!. Come in and ENJOY!")

    def set_number_served(self, number):
        if number > self.number_served:
            self.number_served = number
        else:
            print(f"we are totally booked")

    def increment_number_served(self, additional_number):
        if additional_number>= 0:
            self.number_served += additional_number
        else:
            print("unavailable")



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

user1 = User("loveth", "edeugwu", "21", "female")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

user1.reset_login_attempts()
print("{user1.login_attempts}")



restaurant = Restaurant("Genesis", "Intercontinental")
print(restaurant.number_served) 
restaurant.set_number_served(20)
print(restaurant.number_served)
restaurant.increment_number_served(10)
print(restaurant.number_served)
