# Create a function that receives three parameters and calculates a result depending on operator.
# The operator can be  'multiply', 'divide', 'add', 'subtract' .
# The input comes as three parameters – two integers and an operator as a string.
#
# Input	        Output
# subtract      1
# 5
# 4


def calc_function(operand, x, y):
    if operand == "multiply":
        result = x * y
    elif operand == "divide":
        result = x / y
    elif operand == "add":
        result = x + y
    elif operand == "subtract":
        result = x - y

    return int(result)


operation = input()
first_param = int(input())
second_param = int(input())
print(calc_function(operation, first_param, second_param))
