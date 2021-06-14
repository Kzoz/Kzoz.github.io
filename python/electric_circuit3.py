import time 
import random

t2_bridge = 0
push_btn = cr1_coil = t2_coil = t1_coil = t1 = None

def starter(): 
    global push_btn
    user_inp = int(input("Turn Switch ON?"))
    if user_inp == 1:
        push_btn = 1
        
def initialize():
    global push_btn
    global t2_bridge
    if push_btn == 1:
        t2_bridge = 0

        
def first_block():
    global t1_coil
    global t2_coil
    global cr1_coil
    global t2_bridge
    global t1
    if t2_bridge == 0:
        cr1_coil = 1
        t1_coil = 1
        if t1_coil == 1:
            t1 = 1
            t2_coil = 1
    while t2_coil ==1:
        t2_brdige = 1
        break
    
def second_block():
    global cr1_coil
    lamp1 = lamp2 = None
    if cr1_coil == 1 and t2_bridge == 0:
        print("Lamp1 is ON")
        time.sleep(2)
    elif cr1_coil != 1 and t2_bridge != 0:
        print("Lamp1 is OFF")
        time.sleep(2)
    if t1 == 1:
        print("Lamp2 is ON")
    else:
        print("Lamp2 is OFF")

def the_program():
    global t2_bridge
    cnt = 5
    while cnt > 0:
        starter()
        initialize() 
        t2_bridge = int(random.randint(0,1))
        first_block()
        second_block()
        cnt-=1