# Explosions are marked with '>'. Immediately after the mark, there will be an integer, which signifies the strength of the explosion.
# You should remove x characters (where x is the strength of the explosion), starting after the punch character ('>').
# If you find another explosion mark ('>') while you’re deleting characters, you should add the strength to your previous explosion.
# When all characters are processed, print the string without the deleted characters.
# You should not delete the explosion character – '>', but you should delete the integers, which represent the strength.


def explosion_func(text):
    text_list = [char for char in text]
    explosion_power = 0
    for index in range(len(text_list)):
        if text_list[index] == ">" and index + 1 < len(text_list):
            explosion_power += int(text_list[index + 1])
            for i in range(explosion_power):
                if index + 1 + i < len(text_list) and text_list[index + 1 + i] != ">":
                    text_list[index + 1 + i] = 0
                    explosion_power -= 1
                else:
                    break
    return "".join(each for each in text_list if each != 0)


text_input = input()
print(explosion_func(text_input))
