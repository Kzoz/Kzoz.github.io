import random
import time

def light_system(push_btn):
    relay, self_mntn,kill_btn,cnt = 0,0,0,0
    
    if push_btn == 0:
        pass
    elif push_btn == 1:
        relay = 1
        self_mntn = 1
        while self_mntn == 1:
            relay = self_mntn
            push_btn = int(input("Still ON? "))
            kill_btn = int(input(" Turn off the lights? "))
            if cnt >=2:
                break
            if kill_btn == 1:
                self_mntn = 0
                relay = self_mntn
                break
            else:
                time.sleep(5)
                cnt +=1
    if self_mntn == 1:
        print("Lights will remain ON")
    elif self_mntn == 0:
        print("Lights OFF")

light_system(1)

#unknown = int(random.randint(0,1))

def and_or(s1,s2,s3,s4,s5):

    if s1 == 1 or s2 == 1 or s3 == 0:
        if s4 == 1 and s5 == 0:
            print("Lights are on")
        else:
            print("Lights OFF")
    else:
        None

and_or(1,1,1,1,1)