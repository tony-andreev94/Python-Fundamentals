# 7. Decipher This!
# You are given a secret message you need to decipher. Here are the things you need to know to decipher it:
# For each word:
#   •	the second and the last letter are switched (e.g. Hello becomes Holle)
#   •	the first letter is replaced by its character code (e.g. H becomes 72)

# Input	                    Output
# 72olle 103doo 100ya	    Hello good day
# 82yade 115te 103o	        Ready set go

message = input().split(' ')

for each_item in message:
    text = each_item.strip('0123456789')
    print(text)
    digits = each_item[:len(each_item) - len(text)]
    if len(text) > 1:
        new_string = chr(int(digits)) + text[-1:] + text[1:-1] + text[0]
    else:
        new_string = chr(int(digits)) + text[-1:] + text[1:-1]
    print(new_string, end=" ")