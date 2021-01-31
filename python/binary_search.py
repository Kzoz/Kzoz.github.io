def binary_search(sequence, index):
    strt = 0
    nd = len(sequence)-1
    while strt <= nd:
        mid_index = strt + (strt + nd)//2
        mid_value = sequence[mid_index]
        if mid_value == index:
            return mid_index
        elif index < mid_value:
            nd = mid_index-1 
        else:
            strt = mid_index+1
    return None
    


