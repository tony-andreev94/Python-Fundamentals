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


def calculator(operand, a, b):
    operand_mapping = {
        "multiply": multiply,
        "divide": divide,
        "subtract": subtract,
        "add": add
    }
    function = operand_mapping[operand]
    return function(a, b)


operation = input()
first_param = int(input())
second_param = int(input())
print(calculator(operation, first_param, second_param))