def binary_search(lst, elem):
    start_point = 0
    end_point = len(lst)-1
    while start_point <= end_point:
        mid_index = start_point + (end_point - start_point)//2
        mid_val = lst[mid_index]
        if mid_val == elem:
            return mid_index
        elif elem < mid_val:
            end_point = mid_index-1
        else:
            start_point = mid_index+1
    return None

lst_a = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(lst_a,4))
