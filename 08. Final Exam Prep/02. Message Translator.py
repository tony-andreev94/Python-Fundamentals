# Message Translator
# https://judge.softuni.bg/Contests/Practice/Index/1929#1

import re

n = int(input())
command_regex = r"(?<=!)[A-Z][a-z]{2,}(?=!:)"
message_regex = r"(?<=\[)[A-Za-z]{8,}(?=\])"
end_result = []

for i in range(n):
    command = input()
    c_result = re.findall(command_regex, command)
    if len(c_result) > 0:
        m_result = re.findall(message_regex, command)
        if len(m_result) > 0:
            for each in m_result[0]:
                end_result.append(ord(each))
            print(f"{c_result[0]}: ", end="")
            for each in end_result:
                print(each, end=" ")
            print()
        else:
            print("The message is invalid")
    else:
        print("The message is invalid")
