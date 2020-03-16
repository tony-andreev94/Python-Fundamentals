# the same task with a recursive solution


def repeat_string(string, reps):
    if reps < 1:
        return ""
    return string + repeat_string(string, reps=reps-1)


string_to_repeat = input()
repetitions = int(input())
print(repeat_string(string_to_repeat, repetitions))
