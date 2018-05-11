from Queue import QueueImplementation


def hotpotato(listname,num):
    q1 = QueueImplementation.Queue()
    j=num
    for i in range(0,len(listname)):
        q1.enqueue(listname[i])

    while q1.size()>1:
        # j = num
        if j==0:
            q1.dequeue()
            print (q1.items)
            j=num

        for i in range(j,0,-1):
            if q1.size()!=1:
                q1.enqueue(q1.dequeue())
                print(q1.items)
                j = j - 1



    print(q1.dequeue())



listname=['Bineet','Saanvi','Ishani']
num = 2

hotpotato(listname,num)