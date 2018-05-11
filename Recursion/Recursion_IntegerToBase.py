def converttobase(input,base):
    convertString = "0123456789ABCDEF"
    if input < base:
        return convertString[input]
    else:
        q = input // base
        r = input%base
        return converttobase(q,base)+convertString[r]


print(converttobase(100,10))