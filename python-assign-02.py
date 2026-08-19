# # page108
# # question1
# guest=["abigail","rita","chidimma","bonavee","steph"]
# for guest in guest:
# #     print (f"Hello {guest.title()}, you are cordially invited to my party")

#     # question2
# guest = ["abigail","rita","chidimma","bonavee","steph"]
# for guest in guest:
#     print(f"Dear {guest}, I would be honored if you could join me for dinner.")
# cancelled = "steph"
# print(f"\nUnfortunately, {cancelled} can't make the dinner.")
# guest = (1,"amara")

# for guest in guest:
#     print(f"\nDear {guest}, I would be honored if you could join me for dinner.")

# question3
# guest = ["abigail","rita","chidimma","bonavee","steph"]
# print("Good news everyone! I found a bigger dinner table, so we have more space.")
# guest.insert(0, "kosy")        
# guest.insert(2, "daniel")       
# guest.append("david")       

# for guest in guest:
#     print(f"\nDear {guest}, I would be honored if you could join me for dinner.")
#     print("I am so sorry, but I can invite only two people for dinner.")

# while len(guest) > 2:
#     uninvited = guest.pop()
#     print(f"Sorry, {uninvited}, I can't invite you to dinner.")
#     print(f"\nDear {guest[0]}, you are still invited to dinner.")
#     print(f"Dear {guest[1]}, you are still invited to dinner.")


# del guest[1]
# del guest[0]
# print(f"Final guest list: {guest}")


# page113
# question1
places = ["morocco", "Paris", "austria", "germany", "canada"]
print("Original order:")
print(places)

print("\nAlphabetical order (temporary):")
print(sorted(places))

print("\nVerify still in original order:")
print(places)

print("\nReverse-alphabetical order (temporary):")
print(sorted(places, reverse=True))

print("\nVerify still in original order:")
print(places)

places.reverse()
print("\nOrder has been reversed (permanent):")
print(places)

places.reverse()
print("\nReversed back to original order:")
print(places)

places.sort()
print("\nSorted in alphabetical order (permanent):")
print(places)

places.sort(reverse=True)
print("\nSorted in reverse-alphabetical order (permanent):")
print(places)

# questio2
guest = [""abigail","rita","chidimma","bonavee","steph""]
num_guest = len(guest)
print(f"I am inviting {num_guest} wonderful people to dinner tonight.")

# question3
languages = ["english", "igbo", "hausa", "french", "spanish"]
print(f"Initial list: {languages}")
print(f"The first language in the list is: {languages[0]}")


languages[3] = "french"
print(f"Modified 'french' to 'yoruba': {languages}")

languages.append("Swift")
print(f"Appended 'Swift': {languages}")

languages.insert(1, "Java")
print(f"Inserted 'Java' at index 1: {languages}")

del languages[2]
print(f"Deleted item at index 2 ('JavaScript'): {languages}")

popped_language = languages.pop()
print(f"Popped last item ('{popped_language}'): {languages}")

languages.remove("C++")
print(f"Removed 'C++' by value: {languages}")

print(f"Temporarily sorted: {sorted(languages)}")
print(f"Verified original list order: {languages}")

languages.reverse()
print(f"Permanently reversed order: {languages}")

languages.sort()
print(f"Permanently sorted alphabetically: {languages}")

total_count = len(languages)
print(f"The final list has a total of {total_count} languages.")


# page134
# question1
for number in range(1, 21):
    print(number)

# question2
numbers = list(range(1, 1000001))

for number in numbers:
    print(number)

# question3
numbers = list(range(1, 1000001))

print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}")

# question4
odd_numbers = list(range(1, 20, 2))

for number in odd_numbers:
    print(number)


# question5
threes = list(range(3, 31, 3))

for number in threes:
    print(number)

# question6
cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)

# question7
cubes = [value**3 for value in range(1, 11)]

print(cubes)

# page141
# question1
my_foods = ['pizza', 'falafel', 'carrot cake', 'tacos', 'cannoli']

print("The first three items in the list are:")
print(my_foods[:3])

print("\nThree items from the middle of the list are:")
print(my_foods[1:4])


print("\nThe last three items in the list are:")
print(my_foods[-3:])

# question2
pizzas = ['pepperoni', 'margherita', 'bbq chicken']

friend_pizzas = pizzas[:]

pizzas.append('supreme')

friend_pizzas.append('veggie')


print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(f"- {friend_pizza}")

# question3
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = ['pizza', 'falafel', 'cannoli']

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)


# page145
# question1
menu = ('rice', 'beans', 'chicken', 'plantain', 'yam')

print("Original menu:")
for food in menu:
    print(food)

menu = ('jollof rice', 'beans', 'fish', 'plantain', 'yam')

print("\nRevised menu:")
for food in menu:
    print(food)

# paage161
# question1
bike = 'yamaha'
print("Is bike == 'yamaha'? I predict True.")
print(bike == 'yamaha')

print("\nIs bike == 'honda'? I predict False.")
print(bike == 'honda')

age = 25
print("\nIs age == 25? I predict True.")
print(age == 25)

print("\nIs age != 25? I predict False.")
print(age != 25)

fruits = ['apple', 'banana', 'cherry']
print("\nIs len(fruits) == 3? I predict True.")
print(len(fruits) == 3)


print("\nIs len(fruits) < 2? I predict False.")
print(len(fruits) < 2)

is_weekend = True
print("\nIs is_weekend == True? I predict True.")
print(is_weekend == True)

print("\nIs is_weekend == False? I predict False.")
print(is_weekend == False)

username = 'coder123'
print("\nIs username.lower() == 'coder123'? I predict True.")
print(username.lower() == 'coder123')

print("\nIs username == 'Coder123'? I predict False.")
print(username == 'Coder123')

city = 'Tokyo'
print("\nIs city == 'Tokyo'? I predict True.")
print(city == 'Tokyo')

print("Is city != 'Tokyo'? I predict False.")
print(city != 'Tokyo')

pet = 'Golden Retriever'
print("\nIs pet.lower() == 'golden retriever'? I predict True.")
print(pet.lower() == 'golden retriever')

print("Is pet.lower() == 'Golden Retriever'? I predict False.")
print(pet.lower() == 'Golden Retriever')

score = 85
print("\nIs score > 80? I predict True.")
print(score > 80)

print("Is score < 50? I predict False.")
print(score < 50)

print("Is score >= 85? I predict True.")
print(score >= 85)

print("Is score <= 70? I predict False.")
print(score <= 70)

# Tests using the and k
temperature = 22
humidity = 45

print("\nIs temperature > 20 and humidity < 50? I predict True.")
print(temperature > 20 and humidity < 50)

print("Is temperature > 30 or humidity > 80? I predict False.")
print(temperature > 30 or humidity > 80)

toppings = ['mushrooms', 'onions', 'pineapple']
print("\nIs 'mushrooms' in toppings? I predict True.")
print('mushrooms' in toppings)

print("\nIs 'pepperoni' not in toppings? I predict True.")
print('pepperoni' not in toppings)

print("Is 'onions' not in toppings? I predict False.")
print('onions' not in toppings)

# page171
# question1
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")

alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")

# question2
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points!")

alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points!")

# question3
alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

alien_color = 'yellow'
if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

alien_color = 'red'
if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

# queestion4
age = 25
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

# question5
favorite_fruits = ['bananas', 'apples', 'strawberries']

if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'blueberries' in favorite_fruits:
    print("You really like blueberries!")
if 'strawberries' in favorite_fruits:
    print("You really like strawberries!")
if 'peaches' in favorite_fruits:
    print("You really like peaches!")

# page177
# question1
usernames = ['jaden', 'sarah', 'admin', 'chris', 'emma']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")

# question2
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

# question3
current_users = ['john', 'Mary', 'admin', 'Peter', 'lucas']

new_users = ['LUCAS', 'sarah', 'JOHN', 'alex', 'kevin']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' is already taken. You will need to enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")

# question4
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

# page228
question1
prompt = "\nEnter a pizza topping (enter 'quit' when you are done): "

while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")


# question2
prompt = "\nPlease enter your age (enter 'quit' to exit): "

while True:
    age_input = input(prompt)
    if age_input.lower() == 'quit':
        break
    
    age = int(age_input)
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")

# question3
topping = ""
while topping.lower() != 'quit':
    topping = input("Enter a topping (or 'quit'): ")
    if topping.lower() != 'quit':
        print(f"Adding {topping} to your pizza.")

prompt = "\nPlease enter your age (enter 'quit' to exit): "

while True:
    age_input = input(prompt)
    if age_input.lower() == 'quit':
        break
    
    age = int(age_input)
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")

topping = ""
while topping.lower() != 'quit':
    topping = input("Enter a topping (or 'quit'): ")
    if topping.lower() != 'quit':
        print(f"Adding {topping} to your pizza.")

active = True
while active:
    topping = input("Enter a topping (or 'quit'): ")
    if topping.lower() == 'quit':
        active = False
    else:
        print(f"Adding {topping} to your pizza.")

while True:
    topping = input("Enter a topping (or 'quit'): ")
    if topping.lower() == 'quit':
        break
    print(f"Adding {topping} to your pizza.")

# question4
x = 1
while x <= 5:
    print(f"Current number: {x}")
    # Missing x += 1 makes this run forever

# page233
# questiion1
sandwich_orders = ['tuna', 'veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")

# question2
sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'turkey', 'pastrami', 'roast beef']
print("Sorry, the deli has run out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")

# question3
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    
    responses[name] = response
    
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, location in responses.items():
    print(f"{name} would like to visit {location}.")

# two_sum question
nums = [2, 7, 11, 15]
target = 9
result = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            result = [i, j]
            break 

print(result) 

