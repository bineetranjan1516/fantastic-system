from Stack import StackImplementation


def checkbalance(string):
    s = StackImplementation.stack()
    xlist = list(string)
    print(xlist)
    for x in range(len(xlist)):
        if xlist[x] in '([{':
            s.push(xlist[x])
            # print(match_symbol(xlist[x], s.peek()))

        elif s.size()==0:
            print("UNBALANCED")
            exit()

        elif match_symbol(xlist[x], s.peek())==True:
            s.pop()




    if s.size() ==0:
        print ("BALANCED")
    else:
        print("UNBALANCED")


def match_symbol(open, close):
    opens = '([{'
    closes = ')]}'
    # print(opens.__contains__(open))
    return opens.__contains__(open) == closes.__contains__(close)

y = '{[()}]'

checkbalance(y)