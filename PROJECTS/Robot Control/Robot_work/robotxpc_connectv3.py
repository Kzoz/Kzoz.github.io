#server + client
#version 3: receiving through sockets (localhost) // vector by vector
#version ionvolving 2 PCs and robot
import os,socket,time,itertools
from datetime import datetime
from threading import Thread


#output the robot work in new file
now = datetime.now()
seq = str(now.strftime("%Y%m%d"))
txtname = "kiroku/robot_kiroku"+seq+".txt"  #create output filename
counter = 1
conn = ""
work = 0

#Client Side
def process(ilst):
    global work
    work = work
    work = 0
    HOST = '192.168.3.5' 
    PORT = 10006  
    global counter
    counter = counter
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sok:
        sok.connect((HOST, PORT)) #connect to Robot
        lst = ilst
        for x in lst: 
            sok.sendall(b''+(x).encode('ascii')) #send values 1 by 1
            time.sleep(0.02)    
            data = sok.recv(1024)
            if data == bytes(b'END\r'):         #3sec for data eval
                now = datetime.now()            #acquire current time
                dt = now.strftime("%Y/%m/%d %H:%M:%S")
                print(dt,"---WORK {num} DONE!---".format(num = counter)) #time work finished at
                time.sleep(3)
                if os.path.exists(txtname):
                    append_write = 'a' 
                else:
                    append_write = 'w' 
                feedbck = open(txtname,append_write)
                if counter == 1:
                    feedbck.write("------------NEW JOB-------------\n")
                feedbck.write(dt)
                feedbck.write("---WORK {num} DONE!---".format(num = counter)) #Log end time in txtfile
                feedbck.write("\n")
                counter += 1
                break
        print('Received from Robot:', repr(data),"\n")
        #feedbck.write("---END---\n")
        work = 1
        feedbck.close()
    
#Check Robot Status   
def status():
    global conn # make conn global to keep using it in status()
    global work 
    work = work
    #with conn:
    while work == 0: # meaning robot is executing tasks
        data = conn.recv(1024)
        if work == 1: # meaning robot task is completed
            work=0
            conn.sendall(b'STS,0\r\n') # ready to receive new data
            return
        if not data:
            break
        conn.sendall(b'STS,1\r\n') #busy!
            

#Server Side
def DataTransfer():
    HOST = '127.0.0.1'
    PORT = 1024
    global conn

    worklist = []
    cmdlist = ["PIC"] #lst of commands (excl. STS)
    kanaList = [1001,1002,1003,1004,1005,1006] #lst of available targets
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    #break
                    s.close()
                    DataTransfer()#----------------*********---------------------
                #while data != (b'STS\r\n'):
                #    conn.sendall((b'STS,2_1\r\n')) => meaning something different from sts has been sent.
                # later on a list of the potential errors (STS,2_x) will be necessary.
                if data == (b'STS\r\n'): #this line will be indentend into the while loop
                    conn.sendall(b'STS,0\r\n') #this line too + break at the next line.
                data = conn.recv(1024)
                if not data:
                    break


                x = data.decode('ascii')
                if x!= '':
                    order = []
                    x=x.rstrip() 
                    x = x.split(',') 
                    x = tuple(x)
                    for i in range(len(x)):
                        if i == 0 and x[i] not in cmdlist or x[i] == "": #verify if the header is correct
                            conn.sendall(b'PIC,1\r\n') #Incorrect Header or Value
                            s.close()
                            DataTransfer()
                            #raise ValueError("データ形式が違います")
                        if i%2 != 0 and int(x[i]) not in kanaList: #verify targets match with KanaList
                            conn.sendall(b'PIC,1\r\n')
                            s.close()
                            DataTransfer()
                            #raise NameError("金物名に誤りがあります")
                        if i > 0 and i %2==0 and int(x[i])<0: # verify if valid number is input
                            conn.sendall(b'PIC,1\r\n')
                            s.close()
                            DataTransfer()
                            #raise ValueError("データ形式が違います")
                    command = x[0]
                    x = x[1:]
                    if len(x)%2 != 0: # verify every kana is paired with a val
                        conn.sendall(b'PIC,1\r\n')
                        s.close()
                        DataTransfer()
                        #raise ValueError("データ形式が違います")
                    defaultList = (("1001","0"),("1002","0"),("1003","0"),("1004","0"),("1005","0"),("1006","0"))
                    y = tuple(itertools.zip_longest(x[0::2], x[1::2])) #pair kana&vals
                    finalList = ()
                    for i in defaultList: # adding received data to default List
                        kanamono, value = i
                        if type(y[0]) is tuple:
                            for j in y:
                                if int(kanamono) == int(j[0]):
                                    value = int(value)
                                    value += int(j[1])
                                    value = str(value)
                        if isinstance(y[0],str):
                            if kanamono == y[0]:
                                value = int(value)
                                value += int(y[1])
                                value = str(value)
                        finalList = (finalList)+((kanamono,value),) #tuple of formatted data
                    kana, amo = zip(*finalList)
                    amo = list(amo)
                    order.append(amo)
                    worklist =[x.strip() for i in order for x in i] #task list to send to rbt
                    for i in worklist: 
                        if i == '':
                            conn.sendall(b'PIC,1\r\n')
                            print('empty val')
                            s.close()
                            DataTransfer()
                            #raise ValueError("データ形式が違います")
                conn.sendall(b'PIC,0\r\n')
                print("Received new data: ",(data.decode('ascii')).rstrip())
                print("\n---STARTING WORK!---")
                #multi-thread for communicating with rbt and answering requests from PC 0
                t1 = Thread(target=process, args=(worklist,))
                t2 = Thread(target=status, args=())#, daemon=True)
                t2.start()
                t1.start()
                t1.join()
                t2.join()

DataTransfer()