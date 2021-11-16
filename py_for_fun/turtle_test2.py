import turtle
bob = turtle.Turtle()

def polygon(t, length,n):
    for i in range(n):
        t.fd(length)
        t.lt(1)

for x in range(10):       
    polygon(bob,1,360)
    bob.lt(36)
turtle.mainloop()
