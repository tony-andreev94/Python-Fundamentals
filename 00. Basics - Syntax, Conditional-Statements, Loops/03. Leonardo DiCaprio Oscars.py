# Write a program that receives a single integer number and prints different messages depending on the number:
# -	If Oscar is 88 - "Leo finally won the Oscar! Leo is happy".
# -	If Oscar is 86 - "Not even for Wolf of Wall Street?!"
# -	If Oscar is not 88 nor 86 (and below 88) - "When will you give Leo an Oscar?"
# -	If Oscar is over 88 - "Leo got one already!"
# Input	        Output
# 88	        Leo finally won the Oscar! Leo is happy
# 86	        Not even for Wolf of Wall Street?!
# 81	        When will you give Leo an Oscar?
# 89	        Leo got one already!

int_input = int(input())

if int_input == 88:
    print(f"Leo finally won the Oscar! Leo is happy")
elif int_input == 86:
    print(f"Not even for Wolf of Wall Street?!")
elif int_input > 88:
    print(f"Leo got one already!")
else:
    print(f"When will you give Leo an Oscar?")
