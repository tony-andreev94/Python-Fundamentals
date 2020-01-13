# You are given two values of the same type as input. The values can be of type int, char of string. 
# Create a function that returns the greater of the two values
# if the values are of type int - we compare numbers, therefore we cast the values to integers
# in all other cases we compare strings lexically(check whose first character has greater ASCII value)


def compare_values(value_1, value_2, value_3=None):
    if value_3 == "int":
        if int(value_1) < int(value_2):
            return value_2
        else:
            return value_1
    else:
        if value_1 < value_2:
            return value_2
        return value_1


if __name__ == "__main__":
    value_type = input()
    first_value = input()
    second_value = input()
    if value_type == 'int':
        result = compare_values(first_value, second_value, "int")
    else:
        result = compare_values(first_value, second_value)
    print(result)
