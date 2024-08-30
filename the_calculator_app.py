# Task 1: Build a basic calculator
# Create a function for each arithmetic operation

import math

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    if num2 ==0:
        return int(0)
    return num1 / num2

# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use
while True:

    User_response = input("Choose what kind of operation you want to perform: 'add', 'subtract', 'multiplication', 'division': ")
    if User_response == 'exit':
        print("Exiting the program")
        break 

    if User_response not in ['add', 'subtract', 'multiplication', 'division']:
        print("Invalid operation, please try again")
        continue

    try:
        num1 = int(input("Enter your first number :"))
        num2 = int(input("Enter the second number: "))
    except ValueError:
        print("Invalid number, please try again")
        continue


    if User_response == 'add':
        result = add(num1,num2)
    elif User_response == 'subtract':
        result = subtract(num1, num2)
    elif User_response == 'multiplication':
        result = multiplication(num1, num2)
    elif User_response == 'division':
        result = division(num1, num2)

    print(f"The result is {result}")
# Task 3: Ensure your code can handle divisions by zero and other potential errors, so if you divide by 0,
#  there is error handling set up to prevent an error form showing in the console.

# To fix that error, What i did was set the if statement ==0 and return int(0)