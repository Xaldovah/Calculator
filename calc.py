#!/usr/bin/python3


import math


def addition(a, b):
    """Returns the sum of two numbers."""
    return a + b


def subtraction(a, b):
    """Returns the difference between two numbers."""
    return a - b


def multiplication(a, b):
    """Returns the product of two numbers."""
    return a * b


def division(a, b):
    """Performs division between two numbers and returns the quotient."""
    return a / b


def power(a, b):
    """Calculate the exponentiation of the base to the power of the exponent"""
    return a ** b


def modulo(a, b):
    """Returns the remainder of the division between two numbers."""
    return a % b


def root(a, b):
    """Calculates the bth root of a number."""
    return a ** (1 / b)


def square_root(a):
    """Calculates the square root of a number."""
    return math.sqrt(a)


def cube_root(a):
    """Calculates the cube root of a number."""
    return a ** (1 / 3)


def factorial(a):
    """Calculates the factorial of a number."""
    return math.factorial(a)


def exponent(a, b):
    """Calculates the exponential value of a to the power of b."""
    return math.exp(a) ** b


def square(a):
    """Calculates the square of a number."""
    return a ** 2


def cube(a):
    """Calculates the cube of a number."""
    return a ** 3


def hypotenuse(a, b):
    """Calculates the length of the hypotenuse of a right triangle."""
    return math.sqrt(a ** 2 + b ** 2)


print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Modulo")
print("7. Root")
print("8. Square Root")
print("9. Cube Root")
print("10. Factorial")
print("11. Exponent")
print("12. Square")
print("13. Cube")
print("14. Hypotenuse")

# Dictionary mapping choices to functions
operations = {
    '1': addition,
    '2': subtraction,
    '3': multiplication,
    '4': division,
    '5': power,
    '6': modulo,
    '7': root,
    '8': square_root,
    '9': cube_root,
    '10': factorial,
    '11': exponent,
    '12': square,
    '13': cube,
    '14': hypotenuse
}


while True:
    choice = input("Enter choice (1-14): ")
    if choice in operations:
        break
    print("Invalid input. Please enter a valid choice.")

while True:
    try:
        num1 = float(input("Enter first number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if choice in ['8', '9', '10', '12', '13']:
    result = operations[choice](num1)
    print("Result:", result)
else:
    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    result = operations[choice](num1, num2)
    print("Result:", result)
