# class Restaurant:
#     """Initializing restaurant"""
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print (f"Welcome to {self.restaurant_name}, there is varity of {self.cuisine_type} food")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name}, is now open!. Come in and ENJOY!")


# resturant = Restaurant("Genesis", "Intercontinental")
# print(resturant.restaurant_name)
# print(resturant.cuisine_type)
# resturant.describe_restaurant()
# resturant.open_restaurant()

# restaurant1 = Restaurant("Hiltop", "native")
# print(restaurant1.restaurant_name)
# print(restaurant1.cuisine_type, "\n")
# restaurant1.describe_restaurant()
# restaurant1.open_restaurant()

# restaurant2 = Restaurant("Celebrity", "Chinese")
# print(restaurant2.restaurant_name)
# print(restaurant2.cuisine_type, "\n")
# restaurant2.describe_restaurant()
# restaurant2.open_restaurant()

# restaurant3 = Restaurant("Heaven", "Russian")
# print(restaurant3.restaurant_name)
# print(restaurant3.cuisine_type, "\n")
# restaurant3.describe_restaurant()
# restaurant3.open_restaurant()

# restaurant1.describe_restaurant
# restaurant2.describe_restaurant
# restaurant3.describe_restaurant

# exercise 9.3
class User:
    def __init__(self, first_name, last_name, age,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
            print(f"This is {self.first_name} {self.last_name} {self.age} {self.gender}, that works with us as a software engineer")

    def greet_user(self):
            print(f"welcome {self.first_name}")

user1 = User("loveth", "edeugwu", "21", "female")
# print(user1.first_name, user1.last_name, user1.gender, user1.age, "\n")
user1.describe_user()
user1.greet_user()

user2 = User("amara", "okeke", 50, "male")
# print(user1.first_name, user1.last_name, user1.gender, user1.age, "\n")
user2.describe_user()
user2.greet_user()

user3 = User("rita", "nwamma", "female", 27)
# print(user1.first_name, user1.last_name, user1.gender, user1.age, "\n")
user3.describe_user()
user3.greet_user()
