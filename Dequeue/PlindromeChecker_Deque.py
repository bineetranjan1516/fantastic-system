from Dequeue import DequeueImplementation


def palindromchecker(x):
    dq = DequeueImplementation.Deque()
    palindrome = True
    for i in x:
        dq.addRear(i)

    for j in range(0,dq.size()//2):
        if dq.removeFront()!=dq.removeRear():
            palindrome=False

    print (palindrome)


x = "radar"

palindromchecker(x)