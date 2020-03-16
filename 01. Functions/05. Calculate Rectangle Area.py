# Create a function that calculates and returns the area of a rectangle by given width and height:
#
# Input	    Output
# 3         12
# 4
#
# 6         12
# 2


def rectangle_func(a, b):
    return a * b


side_a = int(input())
side_b = int(input())

print(rectangle_func(side_a, side_b))
