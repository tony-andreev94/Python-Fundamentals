# Write a program that translates messages from Morse code to English (capital letters).
# The words will be separated by a space (' '). There will be a '|' character which you should replace with ' ' (space).


def morse_to_english(text):
    morse_dictionary = {'.-': 'A', '-...': 'B',
                        '-.-.': 'C', '-..': 'D', '.': 'E',
                        '..-.': 'F', '--.': 'G', '....': 'H',
                        '..': 'I', '.---': 'J', '-.-': 'K',
                        '.-..': 'L', '--': 'M', '-.': 'N',
                        '---': 'O', '.--.': 'P', '--.-': 'Q',
                        '.-.': 'R', '...': 'S', '-': 'T',
                        '..-': 'U', '...-': 'V', '.--': 'W',
                        '-..-': 'X', '-.--': 'Y', '--..': 'Z'
                        }
    list_of_morse_words = text.split(" | ")
    list_of_english_words = []
    for each_word in list_of_morse_words:
        char_list = each_word.split(" ")
        word = ""
        for char in char_list:
            if char in morse_dictionary.keys():
                word += morse_dictionary[char]
        list_of_english_words.append(word)
    return list_of_english_words


morse_code = input()
print(*morse_to_english(morse_code))

