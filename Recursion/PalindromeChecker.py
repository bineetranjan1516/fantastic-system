def checkpalindrom(input_string):
    if len(input_string)<1:
        return True
    else:
        if input_string[0]==input_string[-1]:
            return checkpalindrom(input_string[1:-1])
        else:
            return False


print (checkpalindrom("radar"))