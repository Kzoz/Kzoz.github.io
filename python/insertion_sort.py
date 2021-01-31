def insertionsort(lst):
    index_len = range(1,len(lst))
    for i in index_len:
        to_sort = lst[i]

        while lst[i-1] > to_sort and i >0:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i = i-1

    return lst

lst_a = [2,3,7,5,4]
print(insertionsort(lst_a))