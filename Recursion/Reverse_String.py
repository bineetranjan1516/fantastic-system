def reversestring(input_string):
    if len(input_string)==1:
        return input_string
    else:
        return reversestring(input_string[1:])+input_string[0]


print(reversestring("Isha Roy"))