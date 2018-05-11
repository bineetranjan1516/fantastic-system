from Stack import StackImplementation


def converttobinary(i):
    s= StackImplementation.stack()

    # q = quote_rem(i)[0]
    # r = quote_rem(i)[1]
    q,r = quote_rem(i)
    s.push(r)
    while q>0:
        q,r = quote_rem(q)
        s.push(r)

    t = StackImplementation.stack()

    while s.size()>=1:
        t.push(s.peek())
        s.pop()

    while t.size()>=1:
        print (t.size())
        # print(t.peek(),end='')
        t.pop()




def quote_rem(x):
    q = x // 2
    r = x - q * 2
    # print(q,r)

    return q,r



x = 5
print(converttobinary(x))