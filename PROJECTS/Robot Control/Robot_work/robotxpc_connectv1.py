#version 1
#data contained in tuple of tuples
#demarkated by commas
import os,socket,json,time

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

f = open(r'%s' % name, 'r') #open file
order = []
for x in f:
    print(x)
    x=x.rstrip()    #organize file
    y = eval(x)     # turn str to tuple
    kana, amo = zip(*y) 
    amo = list(amo) # get values only
    downlst = [str(y) for y in amo]
    order.append(downlst) # add values to new list
print(order)

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
    lst = order
    counter = 1
    for y in lst:
        for x in y: 
            s.sendall(b''+(x).encode('ascii')) #send values 1 by 1
            time.sleep(0.02)    
            data = s.recv(1024)
            if data == bytes(b'END\r'):         #3sec for data eval
                print("----WORK {num} DONE!----".format(num = counter))
                counter += 1
                time.sleep(3)
    print('Received', repr(data))