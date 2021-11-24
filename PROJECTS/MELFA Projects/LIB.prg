1 '--------------------Useful functions-----------------
2 'Def FNMOD(MX,MY) = MX-(MY*Int(MX/MY)) ' To calculate Modulo
3 '''''''''''''''''''''''''''''''''''''''''''''''''''''''''
4 Function Main
5     M100 = Modulo(MX, MY) 'Modulo(Dividend, Divisor)
6     M101 = Exponent(Mbase, Mpower) 'Exponent(Base, Exponent or power)
7     Position()
8 FEnd
9 '-----------Modulo Function--------------
10 Function M! Modulo(ByVal MX, ByVal MY)
11     Msum = 0
12     Msum = MX-(MY*Int(MX/MY))
13     Modulo = Msum
14     Exit Function
15 FEnd
16 '
17 '-----------Exponent Function------------
18 Function M! Exponent(ByVal Mbase, ByVal Mpower)
19     Mres = 1
20     For M3 = 1 To Mpower
21         Mres = Mres*Mbase
22     Next M3
23     Exponent = Mres
24     Exit Function
25 FEnd
26 '
27 '----------TEST-----------
28 'EBRead #1,,MNUM1,PVS1,MID1,MNUM2,PVS2,MID2,MNUM3,PVS3,MID3
29 'Dly 0.1
30 'MID = 0
31 'Dim MLISTS!(3)
32 'MLISTS(1) = (MNUM1,PVS1)
33 'MLISTS(2) = (MNUM2,PV32)
34 'MLISTS(3) = (MNUM2,PVS3)
35 '
36 'If MLISTS(1) = 1 Then
37 '    MNUM = MNUM1
38 '    PVS = PVS1
39 '    MID = MID1
40 '    Break
41 '[ElseIf MLISTS(2) = 1 Then
42 '    MNUM = MNUM2
43 '    PVS = PVS2
44 '    MID = MID2
45 '    Break
46 '    ]
47 '[ElseIf MLISTS(3) = 1 Then
48 '    MNUM = MUM3
49 '    PVS = PVS3
50 '    MID = MID3
51 '    Break
52 '    ]
53 'EndIf
P200=(+500.10,-0.00,+538.21,+180.00,-0.10,-179.52)(7,0)
P300=(+100.10,-0.00,+538.21,+180.00,-0.10,-179.52)(7,0)
