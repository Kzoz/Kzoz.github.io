def binarysearch(lst, index):
    begin_index = 0
    end_index = len(lst)-1

    while begin_index <= end_index:
        mid_index = begin_index + (end_index-begin_index)//2
        mid_val = lst[mid_index]
        if mid_val == index:
            return mid_index 
        elif index < mid_val:
            end_index = mid_index-1
        else:
            begin_index = mid_index+1
    return None

lst_a = [1,2,3,4,5,6,7,8,9,10,11]
print(binarysearch(lst_a, 8))