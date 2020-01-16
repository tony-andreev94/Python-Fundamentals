# Write a program that reads a floating-point number and prints "zero" if the number is zero.
# Otherwise, print "positive" or "negative".
# Add "small" if the absolute value of the number is less than 1, or "large" if it exceeds 1 000 000
# Input	            Output
# 25	            positive
# 0.7	            small positive
# 435247392.921	    large positive
# -0.005	        small negative
# -103.21	        negative

number = float(input())
result = None

if number == 0:
    result = 'zero'
elif number > 0:
    result = 'positive'
    if abs(number) < 1:
        result = 'small positive'
    elif abs(number) > 100000:
        result = 'large positive'
elif number < 0:
    result = 'negative'
    if abs(number) < 1:
        result = 'small negative'
    elif abs(number) > 1000000:
        result = 'large negative'

print(result)
