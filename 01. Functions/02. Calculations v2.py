# Create a function that receives three parameters and calculates a result depending on operator.
# The operator can be  'multiply', 'divide', 'add', 'subtract' .
# The input comes as three parameters – two integers and an operator as a string.
#
# Input	        Output
# subtract      1
# 5
# 4


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# operand - parameter
# operation - variable
def calculator(operand, a, b):
    if operand.lower() == "multiply":
        return multiply(a, b)
    elif operand.lower() == "divide":
        return divide(a, b)
    elif operand.lower() == "subtract":
        return subtract(a, b)
    elif operand.lower() == "add":
        return add(a, b)
    else:
        return "invalid input"


operation = input()
first_param = int(input())
second_param = int(input())
print(calculator(operation, first_param, second_param))