# set arr 
#set i in arr where is < arr[0] and > arr[len(arr)-1]
#

#def mountainarray(arr):

#    cnt = 0
#    while len(arr) > 2:
#        for i in range(1,len(arr)-1):
#            if arr[0] >= arr[1] or arr[-1] >= arr[-2]:
#                return False
#            if arr[i] > arr[0] and arr[i] > arr[-1]:
#                cnt += 1
#        if cnt == (len(arr)-2):
#            return True
        
#        else:
#            return False
        

#print(mountainarray([3,5,5])) #ppp = [3,5,5]



def mountainvalid(arr):
    mountain = True
    if len(arr) < 3:
        return False
    if arr[0] > arr[1]:
        return False
    if arr[-1] > arr[-2]:
        return False
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            mountain = False
        if not mountain and arr[i] <= arr[i + 1]:
            return False
    return True

    
print(mountainvalid([5,6,7,1]))

