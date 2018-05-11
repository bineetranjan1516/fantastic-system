def bubblesort(alist):
    for i in range(1,(len(alist)-1)):
        # print(i)
        j=0
        while j<len(alist)-1:
            # print(j)
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
            j=j+1

    return alist


blist=[54,26,93,17,77,31,44,55,20]

print(bubblesort(blist))