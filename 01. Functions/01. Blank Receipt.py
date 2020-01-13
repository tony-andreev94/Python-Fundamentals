# Create a function that prints a blank cash receipt. The function should invoke three other functions: 
# One for printing the header, one for the body and one for the footer of the receipt. 


def header_function():
    print(f"CASH RECEIPT\n"
          f"------------------------------")


def body_function():
    print(f"Charged to____________________\n"
          f"Received by___________________")


def footer_function():
    print(f"------------------------------\n"
          f"© SoftUni")


if __name__ == "__main__":
    header_function()
    body_function()
    footer_function()
