import time
import random


border, border2,ret = 0,0,0
switch, switch2 = 0,0

def automat():
    global border2
    global switch2
    
    self_mntnt = 0
    if switch ==1 and border2 == 0:
        relay1 = 1
        self_mntn = 1
        print("Sys1 is ON")
    while self_mntn == 1:
        relay1 = self_mntn
        switch2 = int(input("Turn Sys 2 ON?"))
        if switch2 == 1:
            self_mntn = 0
            print("Sys1 is OFF")
            print("Turning Sys2 ON")
            break
        else:
            switch2 = switch2
            break
    return

def automat2():
    global border
    global switch
    
    self_mntn2 = 0
    if switch2 ==1 and border == 0:
        relay2 = 1
        self_mntn2 = 1
    while self_mntn2 == 1:
        relay2 = self_mntn2
        switch = int(input("Do you want to turn Sys1 ON"))
        if switch == 1:
            self_mntn2 = 0
            print("Sys2 is OFF")
            print("Turning Sys1 ON")
            break
        else:
            switch = switch
            break
    return

user_input = int(input("Which Sys to turn ON? 1 or 2: "))
if user_input == 1:
    switch = 1
elif user_input == 2:
    switch2 = 1
else:
    pass
while ret <3:
    automat()
    automat2()
    ret+=1