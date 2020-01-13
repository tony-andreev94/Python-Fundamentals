# Create a function that calculates and returns the area of a triangle by given base and height.
# Use a general formatting with 12 digits after the decimal point (e.g. {area:.12g})


def calculate_area(a, h):
    area = a * h / 2
    return area


if __name__ == "__main__":
    base = float(input())
    height = float(input())
    result = calculate_area(base, height)
    print(f"{result:.12g}")
