def selectionsort(aList):
    num_pass=1
    for i in range(0,len(aList)):
        max_pos = 0
        for j in range(1,len(aList)-num_pass+1):
            if aList[j]>aList[max_pos]:
                max_pos=j
        if(max_pos!=len(aList)-num_pass):
            print("Replacing.." + str(aList[max_pos]) + "with.." + str(aList[len(aList)-num_pass]))
            aList[max_pos],aList[len(aList)-num_pass]=aList[len(aList)-num_pass],aList[max_pos]
            print(aList)
        num_pass=num_pass+1

    return aList



list_sort=[54,26,93,17,77,31,44,55,20]

print(selectionsort(list_sort))