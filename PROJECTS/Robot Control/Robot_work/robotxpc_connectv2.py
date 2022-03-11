#version 2 #non bracket data
#append logs in new(or already existing) .txt file
import os,socket,time,itertools
from datetime import datetime

txt_files = [f for f in os.listdir('.') if f.endswith('.txt')] # find .txt file in directory
if len(txt_files) != 1:
    raise ValueError('テキストファイルが複数あります。1つにしてください。') # if more than 1 file, raise Error

#defining filename and directory
filename = txt_files[0]
direct = "/Users/seisan/Codes/robot/"
name = os.path.join(direct, filename) #obtain filename

with open(name) as filehandle:
    lines = filehandle.readlines() #retrieve all lines in file
with open(name, 'w') as filehandle:
    lines = filter(lambda x: x.strip(), lines) #remove empty lines
    filehandle.writelines(lines)    #write new lines in same file

#output the robot work in new file
now = datetime.now()
seq = str(now.strftime("%Y%m%d"))
txtname = "kiroku/robot_kiroku"+seq+".txt"  #create output filename

f = open(r'%s' % name, 'r') #open file
order = []
worklist = []
for x in f:
    x=x.rstrip()
    x = x.split(',')
    x = tuple(x)
    print(x)
    for i in range(len(x)):
        if i == 0 and x[i] != "PIC" or x[i] == "":
            raise ValueError("データ形式が違います")
    command = x[0]
    x = x[1:]
    if len(x)%2 != 0:
        raise ValueError("データ形式が違います")
    #y = tuple(itertools.zip_longest(x[0::2], x[1::2]))
    #
    defaultList = (("1001","0"),("1002","0"),("1003","0"),("1004","0"),("1005","0"),("1006","0"))
    y = tuple(itertools.zip_longest(x[0::2], x[1::2]))
    finalList = ()
    for i in defaultList:
        kanamono, value = i
        if type(y[0]) is tuple:
            for j in y:
                if int(kanamono) == int(j[0]):
                    value = j[1]
        if isinstance(y[0],str):
            if kanamono == y[0]:
                value = y[1]
        finalList = (finalList)+((kanamono,value),)
    kana, amo = zip(*finalList)
    amo = list(amo)
    order.append(amo)
for i in order:
    worklist.append([x.strip() for x in i])#;print(worklist) if len(order)==len(worklist) else None
for a in worklist: 
    for i in a:
        if i == '':
            raise ValueError("データに誤りがあります。")
print(worklist)
f.close()


print("上記のデータを再度確認してください。\n")
confirm = input("宜しければ Enter を押してください。 ")
if confirm != "":
    raise NameError('作業を停止します。最初からやり直してください。\n') #confirmation
else:
    print("\n 作業を開始します...\n")


HOST = '192.168.3.5' 
PORT = 10006  
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) #connect to Robot
    lst = worklist
    counter = 1
    for y in lst:
        for x in y: 
            s.sendall(b''+(x).encode('ascii')) #send values 1 by 1
            time.sleep(0.02)    
            data = s.recv(1024)
            if data == bytes(b'END\r'):         #3sec for data eval
                now = datetime.now()
                dt = now.strftime("%Y/%m/%d %H:%M:%S")
                print(dt,"---WORK {num} DONE!---".format(num = counter))
                time.sleep(3)
                if os.path.exists(txtname):
                    append_write = 'a' 
                else:
                    append_write = 'w' 
                feedbck = open(txtname,append_write)
                feedbck.write(dt)
                feedbck.write("---WORK {num} DONE!---".format(num = counter))
                feedbck.write("\n")
                counter += 1
    print('Received', repr(data))
    feedbck.write("---END---\n") 

    feedbck.close()