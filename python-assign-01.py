# exercise1
# instructor_name = "alex"
# student_number = "30"
# course_name = "python class"
# print(f"\nThe instructor is {instructor_name.title()},{student_number} {course_name}")

# exercise2
# student_morning = 15
# students_evening = 25
# student_morning,students_evening = students_evening,student_morning 
# print(student_morning)
# print(students_evening)

# exercise3
# python = 25
# java = 18
# AI = 12
# python,java,AI = 25,18,12
# print(python,java,AI)

# exercise4
# age = 21
# course_rating = 4.9
# course_name = "python"
# print(type(age))
# print(type(course_rating))
# print(type(course_name))

# exercise5
# instructor = "lim"
# academy = "lkhibra"
# slogan = "learning python is fun"
# print("The"+ " "+instructor+" " +"at"+" "+ academy+" "+"says: " +slogan)

# exercise6
# string = "100"
# integer = 42
# print(int(string))
# print(str(integer))
# print(type(string))
# print(type(integer))

# exercise7
# float_number = 9.75
# integer = 50
# print(int(float_number))
# print(float(integer))
# print(type(float_number))
# print(type(integer))

# exercise8
# true_int = (int(True))  
# false_int = (int(False)) 
# print("True as interger: ", true_int)
# print("false as interger: ", false_int)
 

# exercise9
# word = ["python","is","amazing",]
# string = " ".join(word)
# print(string)
# list = string.split(" ")

# exercise10
student = {
    "name": "Lkhibra Academy",
    "age": 5,
    "language": "Python"
}

keys = list(student.keys())
values = list(student.values())

print("Keys:", keys)
print("Values:", values)

#exercise11

number1 = 10
number2 = 5

addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2
modulus = number1 % number2

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)

#exercise12
number1 = 10
number2 = 5

print("10 > 5:", number1 > number2)
print("10 < 5:", number1 < number2)
print("10 == 10:", number1 == 10)
print("10 != 5:", number1 != number2)
print("10 >= 5:", number1 >= number2)
print("10 <= 5:", number1 <= number2)


#exercise13
print("True and False:", True and False)
print("True or False:", True or False)
print("Not True:", not True)

#exercise14
number = 10

print("Initial Value:", number)

number += 5
print("After += :", number)

number -= 3
print("After -= :", number)

number *= 2
print("After *= :", number)

number /= 3
print("After /= :", number)

number %= 2
print("After %= :", number)


#exercise15
print("5 & 3 =", 5 & 3)
print("5 | 3 =", 5 | 3)
print("5 ^ 3 =", 5 ^ 3)
print("5 << 1 =", 5 << 1)
print("5 >> 1 =", 5 >> 1)

#exercise16
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")

#exercise17
a, b, c = map(int, input("Enter three numbers: ").split())

if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
else:
    largest = c

print(f"The largest number is {largest}.")

#exercise18
year = int(input("Enter a year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

 #exercise19
score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} -> Grade: {grade}")

#exercise20
email = "john@example.com"

domain = email.split("@")[1]

print("Domain:", domain)

#exercise21
review = "The quality of this product is good. The quality is impressive and the quality is excellent."

print("The word 'quality' appears", review.count("quality"), "times.")

#exercise22
item1 = "Laptop"
price1 = 1200.99

item2 = "Mouse"
price2 = 25.50

print("Item        Price")
print("-------------------")
print(f"{item1:<12} ${price1:.2f}")
print(f"{item2:<12} ${price2:.2f}")

#exercise23
sentence = "Lkhibra Academy is great"

words = sentence.split()
words.reverse()

sentence = " ".join(words)

print(sentence)

#exercise24
post = "Loving #Python and #Coding at #LkhibraAcademy"

words = post.split()
hashtags = []

for word in words:
    if word.startswith("#"):
        hashtags.append(word)

print("Hashtags:", hashtags)

#exercise25
password = input("Enter your password: ")

has_number = False
has_special = False

special_characters = "!@#$%^&*"

for character in password:
    if character.isdigit():
        has_number = True

    if character in special_characters:
        has_special = True

if len(password) >= 8 and has_number and has_special:
    print("Password is strong.")
else:
    print("Password is not strong.")

#exercise26
text = " Hello   World  !  "

text = text.strip()
words = text.split()
text = " ".join(words)

print(text)

#exercise27
text = "lkhibra academy python training"

text = text.title()

print(text)

#exercise28
text = "I love Python programming"

text = text.replace("Python", "Java")

print(text)

#exercise29
filename = input("Enter a filename: ")

if filename.startswith("report") and filename.endswith(".pdf"):
    print("This is a valid report PDF file.")
else:
    print("This is not a valid report PDF file.")

#exercise30
text = input("Enter a word or phrase: ")

text = text.lower()
text = text.replace(" ", "")

if text == text[::-1]:
    print(text, "is a palindrome!")
else:
    print(text, "is not a palindrome.")