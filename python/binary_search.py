def binary_search(sequence, index):
    strt = 0
    nd = len(sequence)-1
    while strt <= nd:
        mid_index = strt + (nd-strt)//2
        mid_value = sequence[mid_index]
        if mid_value == index:
            return mid_index
        elif index < mid_value:
            nd = mid_index-1 
        else:
            strt = mid_index+1
    return None

lst_a = [1,2,3,4,5,6,7,8,9,10,11]
print(binary_search(lst_a, 8))