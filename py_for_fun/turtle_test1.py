import turtle
bob = turtle.Turtle()






inside = 10
while inside <=100:
    outside = inside + 95
    for i in range(4):
        for a in range(4):
            bob.fd(inside)
            bob.lt(90)
        bob.rt(90)
        for x in range(4):
            bob.fd(outside)
            bob.rt(90)
    inside+=5







turtle.mainloop()