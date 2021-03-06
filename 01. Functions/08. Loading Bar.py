# You will receive a single integer number between 0 and 100 which is divided with 10 without residue (0, 10, 20, 30..)
# Your task is to create a function that visualizes a loading bar depending on that number you have received in the input.
#
# Input	        Output
# 30	        30% [%%%.......]
#               Still loading...
#
# 100	        100% Complete!
#               [%%%%%%%%%%]


def loading_func(percent):
    x = percent / 10
    if x == 10:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f"{number}% [{'%' * int(x)}{'.' * (10 - int(x))}]")
        print("Still loading...")


number = int(input())
loading_func(number)

