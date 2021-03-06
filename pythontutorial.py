print("Hello World")

age = 20
print(age)

age = 22
print(age)

age = 20
price = 19.99 
first_name = "Mr. Doe"
is_online = True
print(first_name + " is " + str(age) + " years old")

age = 20
name ="James Smith"
print(name + ", age " + str(age)+ ", has checked in as a new patient")

name = input("what is your name")
print("Hello " + name)

birth_year = input("Enter your birth year")
age = 2021 - birth_year
print (age)

birth_year = input("Enter your birth year")
age = 2021 - int(birth_year)
print (age)

add1 = input("Enter the first number:")
add2 = input("Enter the second number:")
addSum = int(add1) + int(add2)
print("The sum of " + str(add1) + " and " + str(add2) + " is " + str(addSum))

# The string class contains a lot of built-in methods
course = 'Discover AI'
print(course.find('i'))

# Addition
print("10 + 3 = " + str(10 + 3))

# Subtraction
print("10 - 3 = " + str(10 - 3))

# Multiplication
print("10 * 3 = " + str(10 * 3))

# Division
print("10 / 3 = " + str(10 / 3))

# Division with integer
print("10 //3 = " + str(10 // 3))

# Modulus 
print("10 % 3 = " + str(10 % 3))

# Exponent
print("10 ** 3 = " + str(10 ** 3))

# Augmented operators
x = 10
x += 3
print(x)

x = 10 + 3 * 2
print (x)

# They return boolean (True/False) solutions

# Greater than
print("10 > 3: " + str(10 > 3))
# Greater than or equal to
print("3 >= 3: " + str(10 >= 3))
# Less than
print("10 < 3: " + str(10 < 3))
# Less than or equal to
print("10 <= 3: " + str(10 <= 3))
# Equal
print("10 == 3: " + str(10 == 3))
# Not equal
print("10 != 3: " + str(10 != 3))


# Used for building complex rules and conditions

# Using "and" check that a price is between two values
price = 25
print("Price between 10 and 30: " + str(price > 10 and price < 30))

# Using "or" check that a price is either of two values
price = 25
print("Price is either 10 or 30: " + str(price == 10 or price == 30))

# Using "not" check that a price is less than a value
price = 25
print("Price is less than 30: " + str(not price < 30))

# Used to make decisions

# Print a message if the temperature is > 30
temperature = 35
if(temperature > 30):
    print("It's a hot day")
    print("Drink plenty of water")
# Everything below will be outside of the conditional statement
print ("Done")

temperature = 25
if(temperature > 30):
    print("It's a hot day")
    print("Drink plenty of water")
elif (temperature <= 30 and temperature >= 25):
    print("It's a nice day")
else:
    print("Brrr! It's cold outside!")
    print("Put on a coat.")


weight = input("What is the weight?")
unit = input("Is the weight in kg or lb?")
lb = 0
kg = 0
if(unit.lower() == "kg"):
    kg = int(weight)
    lb = kg * 2.2046
    print(str(kg) + " kg(s) is equal to " + str(lb) + " lb(s)")
elif(unit.lower() == "lb"):
    lb = int(weight) * 0.4536
    print(str(lb) + " lb(s) is equal to " + str(kg) + " kg(s)")
else:
    print("Weight can only be in kg or lb. Try again.")


i = 1
while i <= 1000:
    print(i)
    i = i + 1


# list of names
names = ["Jane", "John", "Mary", "Sam", "Safi"]
print(names)
i = 0
# print the first three names
print("First three names:")
while i < 3:
    print(names[i])
    i += 1
# Add a name at the head of the list
names.insert(0, "Jacky")
print("First name is now: " + names[0])
names[0] = "Jalen"
print("First name is now: " + names[0])

numbers = [1, 2, 3, 4, 5, 6]
# Append
numbers.append(8)
# Insert
numbers.insert(0, 9)
# Remove
numbers.remove(3)
# Clear
numbers.clear()
# In 
print(10 in numbers)
# Len
print (len(numbers))

numbers = [1, 2, 3, 4, 5,]
for item in numbers:
    print (item)

# The function can have 1 to 3 arguments.

# 1. generate numbers up to a value
numbers = range(3)
for number in numbers:
    print(number)

# Immutable (unchangeable) elements
numbers = (1, 2, 3)
