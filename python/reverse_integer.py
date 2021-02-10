#x = 123
x = -123
#x = 120
#x = 0
#x = 9999999999999999 

def reverse(x):
    while x != 0:
        if x > 0 :
            x = int(str(x)[::-1])
            if x > 2**31:
                return 0
            return x
        else:
            x = int(str(x)[::-1].replace('-', ''))
            if - x < -2**31:
                return 0
            return - x
    return 0

print(reverse(x))