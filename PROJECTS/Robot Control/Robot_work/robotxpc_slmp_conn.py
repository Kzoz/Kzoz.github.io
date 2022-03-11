# to write values
# slmp version #non bracket data
#append logs in new(or already existing) .txt file
#send data through PLC

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
    print(x)
    x = x.split(',')
    x = tuple(x)
    y = tuple(itertools.zip_longest(x[0::2], x[1::2]))
    kana, amo = zip(*y)
    amo = list(amo)
    order.append(amo)
for i in order:
    worklist.append([int(x.strip()) for x in i])#;print(worklist) if len(order)==len(worklist) else None
f.close()
print(worklist)

HOST = '192.168.3.250'
PORT = 2000
BUFSIZE = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.settimeout(3)

def reception():
    while True:
        global sock
        sock = sock
        data = [
            0x50,0x00,      #Subheader
            0x00,           #Requested network number
            0xFF,           #Request destination area code
            0xFF,0x03,      #Requested unit I/O number
            0x00,           #Request destination multi-drop area code
            0x0C,0x00,      #Request data length(Set later)
            0x20,0x00,      #Monitoring timer
            0x01,0x04,      #command
            0x01,0x00,      #Subcommand
            0x00,0x00,0x00, #First device number
            0x90,           #Device code
            0x01,0x00       #Device score
        ]

        #Set request data length
        data[7] = len(data[9:]) & 0xFF
        data[8] = (len(data[9:]) >> 16) & 0xFF

        #Send request
        sock.send(bytes(data))

        #Receive response
        res = sock.recv(BUFSIZE)
        rs = ([format(i,'02X') for i in res])
        #print (*[format(i,'02X') for i in res])
        #print(rs)

        time.sleep(2.2)
        if rs[11] == '10':# ['D0', '00', '00', 'FF', 'FF', '03', '00', '03', '00', '00', '00', '10']:
            sock.close()
            break

def activation():
    HOST = '192.168.3.250'
    PORT = 2000
    BUFSIZE = 4096

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.settimeout(3)
    MWData = [
        0x50,0x00,      #Subheader
        0x00,           #Requested network number
        0xFF,           #Request destination area code
        0xFF,0x03,      #Requested unit I/O number
        0x00,           # 
        0x0C,0x00,      #Request data length(Set later)
        0x04,0x00,      #Monitoring timer
        0x01,0x14,      #command(1401H)
        0x01,0x00,      #Subcommand
        0x01,0x00,0x00, #First device number
        0x90,           #Device code for M
        0x01,0x00,      #Device score
        0x10            # 10 to turn on, 01 to turn off
    ]

    #Set request data length
    MWData[7] = len(MWData[9:]) & 0xFF
    MWData[8] = (len(MWData[9:]) >> 16) & 0xFF

    #Send request
    sock.send(bytes(MWData))

    #Receive response
    res = sock.recv(BUFSIZE)
    print (*[format(i,'02X') for i in res])
    sock.close()

    
def transfert(wrklst):
    for i in wrklst:
        HOST = '192.168.3.250'
        PORT = 2000
        BUFSIZE = 4096

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.settimeout(3)
        data = [
            0x50,0x00,      #Subheader
            0x00,           #Requested network number
            0xFF,           #Request destination area code
            0xFF,0x03,      #Requested unit I/O number
            0x00,           # 
            0x0C,0x00,      #Request data length(Set later) #try: 0x0C, 0x00 which is 12 bytes
            0x04,0x00,      #Monitoring timer
            0x01,0x14,      #command(1401H)      #0401 for Read which will be 0x04, 0x01,
            0x00,0x00,      #Subcommand     #similar to 0x00, 0x02?? 
            0x65,0x00,0x00, #First device number #try: 0x64,0x00,0x00 to start from D100 register
            0xA8,           #Device code standing for D
            0x06,0x00,      #Number of device pts #try: 0x06,0x00,  for the 6 types of kanamono being used
            0x00,0x00,      # D0101  # after first device number changes, registers will start with D101 to D106 
            0x00,0x00,      # D0102 # Data[21] = D0101 and so on
            0x00,0x00,      # D0103
            0x00,0x00,      # D0104
            0x00,0x00,      # D0105
            0x00,0x00,      # D0106
        ]


        #Set request data length
        data[7] = len(data[9:]) & 0xFF
        data[8] = (len(data[9:]) >> 16) & 0xFF

        #write user's from D101 which is equal to data[21]
        #verify if data and MWData can be sent throught the same loop.
        i=i
        data[21] = i[0]
        data[23] = i[1]
        data[25] = i[2]
        data[27] = i[3]
        data[29] = i[4]
        data[31] = i[5]
        sock.send(bytes(data))
        res = sock.recv(BUFSIZE)
        print (*[format(i,'02X') for i in res])
        sock.close()
        time.sleep(3)
        #activation()
        #reception()
        #time.sleep(5)

transfert(worklist)