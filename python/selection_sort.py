#have n elem

#take and n[0] and compare to i in the_rest=(n[len(n)])
#if i in the_rest < n[0]
#n[0] = i

def selectionsort(elemlist):

    entire_lst = range(0,len(elemlist)-1)
    for i in entire_lst:
        min_value = i
        for j in range(i+1,len(elemlist)):
            if elemlist[j] < elemlist[min_value]:
                min_value = j
        if min_value != i:
            elemlist[min_value], elemlist[i] = elemlist[i], elemlist[min_value]
    return elemlist

list_a = [4,2,1,6,7,0,4,7,8,1,2,4,9,3]
print(selectionsort(list_a))

        