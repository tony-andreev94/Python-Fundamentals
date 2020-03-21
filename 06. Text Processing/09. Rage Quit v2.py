# Alternative solution of the same task.


def string_builder(text):
    index = 0
    result = ""

    while index < len(text):
        if text[index].isdigit():  # find first digit in the string
            num_str = text[index]  # part of the string that is numeric
            next_index = 1

            if index + 1 < len(text) and text[index + 1].isdigit():  # check if there is another digit afterwards
                num_str += text[index + 1]
                next_index = 2

            number = int(num_str)
            result += text[:index] * number

            if index + 1 >= len(text):
                break

            text = text[next_index + index:]
            index = 0
        else:
            index += 1

    return result.upper()


text_input = input()

print(f"Unique symbols used: {len(set(string_builder(text_input)))}")
print(string_builder(text_input))
