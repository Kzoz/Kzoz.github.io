a,b,x = 1,1,1
n = 0
print("Fibonacci Sequence: ")

while True:
    print(x)
    a = x 
    x += b
    b = a
    n+= 1
    if n >= 8**3:
        break