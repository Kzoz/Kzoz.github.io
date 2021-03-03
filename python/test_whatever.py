def insertion_sort(lst):
    sequence = range(1,len(lst))
    for i in sequence:
        toSort = lst[i]
        while lst[i-1] > toSort and i > 0:
            lst[i-1], lst[i] = lst[i], lst[i-1]
            i -=1
    return lst

lst_a = [2,3,7,5,4]
print(insertion_sort(lst_a))