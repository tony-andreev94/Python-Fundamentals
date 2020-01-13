# Create a function that calculates and returns the value of a number raised to a given power:


def math_power_func(num, pow):
    result = num ** pow
    print(result)


if __name__ == "__main__":
    number = float(input())
    power = float(input())
    math_power_func(number, power)
