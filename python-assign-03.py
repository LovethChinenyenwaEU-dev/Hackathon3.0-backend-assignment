#page 247
#def make_shirt(size,text):
#     print(f"\n{size} {text}")
# make_shirt("god is good", 12)


# def make_shirt(size,text):
#     print(f"\n{size} {text}")
# make_shirt(text="god is good",size= 12)
# make_shirt(size=40,text="i love python")

# def describe_city(city,country):
#     print(f"{city} is in {country}")
# describe_city("reykjavik","icelamd")


# page 255
# question1
# def city_country(city,country):
#     print(f"{city.title()} {country.title()}")
# city_country=("santiago", "chile")

# # question2
# def make_album(musician,album_title,song):
#     albums=f"this is for {musician.title()} {album_title.title()} {song.title()} enjoy!"
#     return albums.title()
# listen=make_album("davido","spwanky","chioma")
# print(listen)

# def make_album(musician, album_title, song_no=" "):
#     if song_no:
#         albums=f"{musician} {song_no} {album_title}"
#     else:
#        albums=f"{musician} {album_title}"
#        return albums.title()
# musician=make_album("davido","chioma",)
# musician=make_album("davido","chioma",song_no=40)
# print(musician)


# question3
# def make_album(musician,album_title):
#     albums = f"{musician} {album_title}"
#     return albums.title()
# while True:
#     print("\ntype the name of your favourite artist:")
#     print("(enter 'w' at any time to quit)")
#     musician=input("album_title name: ")
#     if musician == 'w':
#         break
#     album_title=input("album_title: ")
#     if album_title=='w':
#         break
#     name=make_album(musician, album_title)
#     print(f"\nhello, {name}")

page261
question1
def show_message(messages):
    for message in messages:
        print(message)
text_messages = [
    "Hello! How are you?",
    "Don't forget to buy milk.",
    "See you at 5 PM!",
    "Happy Birthday!"
]
show_messages(text_messages)

question2
def show_messages(messages):
    """Print all messages in the list."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message and move it to sent_messages."""
    print("\nSending messages:")
    while messages:
        current_message = messages.pop(0)
        print(f"Sending: {current_message}")
        sent_messages.append(current_message)

text_messages = [
    "Hello! How are you?",
    "Don't forget to study.",
    "sleep on time",
    "goodmight!"
]
sent_messages = []
send_messages(text_messages, sent_messages)
print("\nFinal Lists Verification")
print(f"Original messages list: {text_messages}")
print(f"Sent messages list: {sent_messages}")

# question3
def send_messages(messages, sent_messages):
    """Print each message and move it to sent_messages."""
    print("\nSending messages:")
    while messages:
        current_message = messages.pop(0)
        print(f"Sending: {current_message}")
        sent_messages.append(current_message)


text_messages = [
    "Hello! How are you?",
    "Don't forget to study.",
    "sleep on time",
    "goodmight!"
]
sent_messages = []
send_messages(text_messages[:], sent_messages)
print("\nFinal Lists Verification")
print(f"Original messages: {text_messages}")
print(f"Sent messages: {sent_messages}")

# page 266
# question1
def make_sandwich(*items):
    """Summarize the sandwich being ordered."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
make_sandwich("roast beef", "cheese", "lettuce", "mayo")
make_sandwich("turkey", "tomatos")
make_sandwich("peanut butter", "egg")

# question2
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
my_profile = build_profile(
    'ebuka', 
    'bonavee',
    location='Nigeria',
    field='computer science',
    hobby='coding'
)

print(my_profile)

# question3
def make_car(manufacturer, model, **car_info):
    """Store information about a car in a dictionary."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car(
    'open roof', 
    'jeep', 
    color='blue', 
    tow_package=True
)
print(car)

# page 342
# question1
print("Give me two numbers, and I will add them.")
first_number = input("First number: ")
second_number = input("Second number: ")

try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("Error: Please enter numbers only, not text!")
else:
    print(f"The sum is: {answer}")

# questio2
print("Enter two numbers to add them together.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number.lower() == 'q':
        break
        
    second_number = input("Second number: ")
    if second_number.lower() == 'q':
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Error: That was not a number. Try again!")
    else:
        print(f"The sum is: {answer}")

# question3
from pathlib import Path

files = ['cats.txt', 'dogs.txt']

for file_name in files:
    path = Path(file_name)
    print(f"\nReading file: {file_name}")
    
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, the file '{file_name}' does not exist in this folder.")
    else:
        print(contents.strip())

# question4
from pathlib import Path

files = ['cats.txt', 'dogs.txt']

for file_name in files:
    path = Path(file_name)
    
    try:
        contents = path.read_text()
        print(f"\nReading file: {file_name}")
        print(contents.strip())
    except FileNotFoundError:
        pass

# question5
from pathlib import Path
path = Path('book.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print("Please make sure your 'book.txt' file is in the correct folder.")
else:
    lowercase_text = contents.lower()
    rough_count = lowercase_text.count('the')
    clean_count = lowercase_text.count('the ')
    
    print(f"Analyzing text from: {path.name}")
    print(f"Number of times 'the' appears (rough): {rough_count}")
    print(f"Number of times 'the ' appears (with space): {clean_count}")


# page192
# question1
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 28,
    'city': 'Enugu'
}

print(f"First Name: {person['first_name']}")
print(f"Last Name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")

# quetion2
favorite_numbers = {
    'amara': 7,
    'bisi': 12,
    'chidimma': 3,
    'tunde': 22,
    'emeka': 9
}

print(f"Amara's favorite number is {favorite_numbers['amara']}.")
print(f"Bisi's favorite number is {favorite_numbers['bisi']}.")
print(f"Chidimma's favorite number is {favorite_numbers['chidimma']}.")
print(f"Tunde's favorite number is {favorite_numbers['tunde']}.")
print(f"Emeka's favorite number is {favorite_numbers['emeka']}.")


# question3
glossary = {
    'string': 'A series of characters treated as text.',
    'list': 'A collection of items kept in a specific order.',
    'dictionary': 'A collection of key-value pairs.',
    'loop': 'A block of code that repeats multiple times.',
    'comment': 'A note in the code that Python ignores.'
}

print(f"string:\n\t{glossary['string']}\n")
print(f"list:\n\t{glossary['list']}\n")
print(f"dictionary:\n\t{glossary['dictionary']}\n")
print(f"loop:\n\t{glossary['loop']}\n")
print(f"comment:\n\t{glossary['comment']}\n")


# page 201
# question1
glossary = {
    'string': 'A series of characters treated as text.',
    'list': 'A collection of items kept in a specific order.',
    'dictionary': 'A collection of key-value pairs.',
    'loop': 'A block of code that repeats multiple times.',
    'comment': 'A note in the code that Python ignores.',
    'key': 'The first item in a key-value pair, used to find data.',
    'value': 'The data linked to a specific key in a dictionary.',
    'conditional test': 'An expression that evaluates to True or False.',
    'boolean': 'A value that can only be True or False.',
    'float': 'A numerical value that contains a decimal point.'
}

for word, meaning in glossary.items():
    print(f"{word}:\n\t{meaning}\n")


# question2
rivers = {
    'nile': 'egypt',
    'niger': 'nigeria',
    'mississippi': 'united states'
}

print("River Sentences")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers Included")
for river in rivers.keys():
    print(river.title())

print("\n--- Countries Included ---")
for country in rivers.values():
    print(country.title())


# question3
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people_to_poll = ['jen', 'obi', 'phil', 'amara', 'sarah', 'tunde']

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for already responding to the poll!")
    else:
        print(f"Hi {person.title()}, you are invited to take our favorite languages poll.")


# page 210
# questio1
person_1 = {
    'first_name': 'amaka',
    'last_name': 'charles',
    'age': 28,
    'city': 'Enugu'
}

person_2 = {
    'first_name': 'Amara',
    'last_name': 'Okonkwo',
    'age': 24,
    'city': 'Lagos'
}

person_3 = {
    'first_name': 'chidimma',
    'last_name': 'mogbo',
    'age': 31,
    'city': 'Abuja'
}

people = [person_1, person_2, person_3]
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"\nName: {full_name}")
    print(f"\tAge: {person['age']}")
    print(f"\tCity: {person['city']}")


# question2
pet_1 = {'animal': 'dog', 'owner': 'steph'}
pet_2 = {'animal': 'cat', 'owner': 'chidimma'}
pet_3 = {'animal': 'parrot', 'owner': 'obi'}
pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"\nPet Details:")
    print(f"\tKind of animal: {pet['animal'].title()}")
    print(f"\tOwner's name: {pet['owner'].title()}")

favorite_places = {
    'chinelo': ['zanzibar', 'paris', 'abuja'],
    'emeka': ['london', 'calabar'],
    'sarah': ['new york']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"- {place.title()}")


# question4
favorite_numbers = {
    'amara':,
    'bisi':,
    'chidimma':,
    'tunde':,
    'emeka': [9, 18, 27]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")


# question5
cities = {
    'lagos': {
        'country': 'nigeria',
        'population': '15 million',
        'fact': 'It is a major financial hub in Africa.'
    },
    'tokyo': {
        'country': 'japan',
        'population': '37 million',
        'fact': 'It is the most populous metropolitan area in the world.'
    },
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'It is known as the City of Light.'
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"\tCountry: {info['country'].title()}")
    print(f"\tApproximate Population: {info['population']}")
    print(f"\tFact: {info['fact']}")


# question6
cities = {
    'lagos': {
        'country': 'nigeria',
        'population': '15.3 million',
        'fact': 'It is a major financial hub in Africa.',
        'currency': 'naira'
    },
    'tokyo': {
        'country': 'japan',
        'population': '37.4 million',
        'fact': 'It is the most populous metropolitan area in the world.',
        'currency': 'yen'
    },
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'It is known as the City of Light.',
        'currency': 'euro'
    }
}

for city, info in cities.items():
    print(f"\n WELCOME TO {city.upper()}!")
    print(f"------------------------------------")
    print(f" Country    : {info['country'].title()}")
    print(f" Population : {info['population']}")
    print(f" Currency   : {info['currency'].title()}")
    print(f" Fun Fact   : {info['fact']}")
print("====================================")

