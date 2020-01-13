# Create a function that prints the sign of an integer number n


def number_check():
    number = int(input())
    if number > 0:
        print(f"The number {number} is positive.")
    elif number < 0:
        print(f"The number {number} is negative.")
    else:
        print(f"The number {number} is zero.")


if __name__ == "__main__":
    number_check()
