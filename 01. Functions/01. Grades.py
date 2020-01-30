# Write a function that receives a grade between 2.00 and 6.00 and prints the corresponding grade in words
# •	2.00 – 2.99 - "Fail"
# •	3.00 – 3.49 - "Poor"
# •	3.50 – 4.49 - "Good"
# •	4.50 – 5.49 - "Very Good"
# •	5.50 – 6.00 - "Excellent"
#
# Input	    Output
# 3.33	    Poor
# 4.50	    Very Good
# 2.99	    Fail


def grade_function(grade_input):
    if 2 <= grade_input <= 2.99:
        return "Fail"
        # result = "Fail"
    elif 3 <= grade_input <= 3.49:
        return "Poor"
        # result = "Poor"
    elif 3.5 <= grade_input <= 4.49:
        return "Good"
        # result = "Good"
    elif 4.5 <= grade_input <= 5.49:
        return "Very Good"
        # result = "Very Good"
    elif 5.5 <= grade_input <= 6:
        return "Excellent"
        # result = "Excellent"

    # return result


if __name__ == "__main__":
    grade = float(input())
    print(grade_function(grade))
