nums = [1,2,3,4,5,6,7]
def yielding(lst):
    for i,j in enumerate(lst):
        yield i
        #return j
print(yielding(nums))