1 '-------------------------------------
2 ' Step 3. Program to adjust the hand camera
3 ' Calibration assistance program HND4.prg
4 '-------------------------------------
5 Def Pos P_CMTL ' Hand camera: Camera center position data
6 Def Pos P_CLPos ' Hand camera: Reference point to start calibration
7 Def Pos P_CMH ' Hand camera: Offset from the surface of the identified workpiece to the imaging point
8 Def Pos P_HVSP1 ' Hand camera: Default imaging point
9 Def Pos P_WRK03 ' Hand camera: Master workpiece grasp position
10 Def Pos P_PVS03 ' Hand camera: Master workpiece identification point
11 Def Pos P_PH03 ' Hand camera: Coefficient for calculating the handling position from the position of the identified workpiece
12 Def Char C_C03 ' Hand camera: COM name
13 Def Char C_J03 ' Hand camera: Job name
14 Def Pos P_PHome ' Safe position
15 Loadset 1,1
16 OAdl On
17 Servo On
18 Wait M_Svo=1
19 '---------------------****---------------------------
20 '
21 'Def variables for palette and *loop count
22 '
23 M1 = 1 'Counter for palette position
24 M50 = 5 'Pallete x
25 M51 = 10 'Palette y
26 M52 = M50*M51 ' Palette total num of stops
27 Def Plt 1,P31,P32,P33,P34,M50,M51,11
28 M10 = 1 'Counter for 2nd palette position & loop count
29 M60 = 2 '2nd Pallete x
30 M61 = 3 '2nd Palette y
31 M62 = M50*M51 ' 2nd Palette total num of stops
32 Def Plt 2, P44,P43,P42,P41,M60,M61,11
33 '
34 '-----------------Test---------------
35 '
36 '
37 '
38 '----------------------------------
39 'Home Position
40 Mov P_PHome
41 '-----------------Hand INIT-----------
42 Dly 1
43 HClose 1
44 Dly 2
45 HOpen 1
46 Dly 0.3
47 '---------------------****---------------------------
48 '
49 *LOOP
50 P100 = Plt 1,M1
51 GoSub *VISION
52 GoSub *PICK
53 GoSub *PLACE
54 *MLP
55 M1 = M1+1
56 If M1 <= M52 Then *LOOP
57 Mov P_PHome
58 Hlt
59 End
60 '---------------------****---------------------------
61 '
62 *VISION
63 Tool P_NTool
64 MCNT=1
65 HOpen 1
66 M_Out(10129)=0
67 M_Out(10128)=1 Dly 0.1
68 Dly 0.5
69 If M_NvOpen(1)<>1 Then
70 NVOpen C_C03$ As #1
71 Wait M_NvOpen(1)=1
72 EndIf
73 NVLoad #1, "Sample"
74 Dly 0.3
75 Mov P100'new palette position replacing 'Mov P_HVSP1
76 Dly 1
77 *RETRY
78 NVRun #1,C_J03$
79 EBRead #1,,MNUM,PVS
80 Dly 0.1
81 If MNUM>=1 Then *OK
82 MCNT=MCNT+1
83 If MCNT>2 Then 'Didn't find any object after 2 loops
84     GoTo *MLP' Move to next palette
85 EndIf
86 Dly 0.2
87 GoTo *RETRY
88 *OK
89 MCNT=1
90 PTRG=P100*P_CMTL*PVS*P_PH03 'PTRG=P_HVSP1*P_CMTL*PVS*P_PH03
91 Return
92 '---------------------****---------------------------
93 '
94 *PICK
95 Mov PTRG,-100
96 Dly 0.5
97 HOpen 1
98 Dly 0.5
99 Mvs PTRG,20
100 Dly 0.6
101 HClose 1
102 Dly 0.5
103 M_Out(10129)=1
104 Dly 0.3
105 Mvs PTRG,-100
106 Dly 0.1
107 Return
108 '---------------------****---------------------------
109 '
110 *PLACE
111 '---------Launch target(place position) recognition program---------
112 If M_NvOpen(1)<>1 Then
113 NVOpen C_C03$ As #1
114 Wait M_NvOpen(1)=1
115 EndIf
116 NVLoad #1, "Sample2"
117 Dly 2
118 '
119 '----------Loop to find where the items must be put at
120 *BLOOP 'move through palette at each *loop
121 P200 = Plt 2,M10
122 Mov P200'new position
123 Dly 1.7
124 *RETRYS
125 NVRun #1,"sample2.job"
126 EBRead #1,,MNUM,PVS
127 Dly 0.1
128 If MNUM>=1 Then *OKAY
129 MCNT=MCNT+1
130 If MCNT>2 Then
131     M1=M1+1
132     GoTo *NLP' Skip to end function
133 EndIf
134 Dly 0.2
135 GoTo *RETRYS
136 *OKAY
137 MCNT=1
138 PTRGS=P200*P_CMTL*PVS*P_PH03
139 Dly 0.3
140 '
141 '
142 Mov PTRGS,-100
143 Mvs PTRGS,20
144 HOpen 1
145 Dly 0.5
146 M_Out(10129)=0
147 M_Out(10128)=1 Dly 0.1
148 Dly 0.2
149 Mvs PTRGS,-100
150 M10 = M10+1
151 GoTo *FLP
152 *NLP
153 M10 = M10+1
154 If M10<=M62 Then *BLOOP
155 *FLP
156 Return
P_CMTL=(0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00)(,)
P_CLPos=(0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00)(,)
P_CMH=(0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00)(,)
P_HVSP1=(0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00)(,)
P_WRK03=(0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00)(,)
P_PVS03=(0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00)(,)
P_PH03=(0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00)(,)
P_PHome=(0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00)(,)
P31=(+399.76,-276.02,+506.91,+180.00,+0.00,+175.90)(7,0)
P32=(+654.24,-276.02,+506.91,-180.00,+0.00,+175.90)(7,0)
P33=(+654.24,+304.97,+506.91,-180.00,+0.00,+175.90)(7,0)
P34=(+399.76,+304.97,+506.91,+180.00,+0.00,+175.90)(7,0)
P44=(+287.85,+238.57,+506.91,-180.00,+0.00,+177.66)(7,0)
P43=(+343.27,+238.57,+506.91,-180.00,+0.00,+177.66)(7,0)
P42=(+343.27,+29.65,+506.91,-180.00,+0.00,+177.66)(7,0)
P41=(+277.83,+29.65,+506.91,+180.00,+0.00,+177.66)(7,0)
P100=(+484.59,-82.36,+506.91,+180.00,+0.00,+175.90,+0.00,+0.00)(7,0)
PVS=(+0.00,+0.00,+0.00,+0.00,+0.00,+0.00,+0.00,+0.00)(0,0)
PTRG=(+452.48,+173.23,+211.47,-180.00,+0.00,+84.03,+0.00,+0.00)(7,0)
P200=(+277.83,+29.65,+506.91,-180.00,+0.00,+177.66,+0.00,+0.00)(7,0)
PTRGS=(+204.23,+31.41,+211.47,+180.00,+0.00,-178.90,+0.00,+0.00)(7,0)
PPUT=(+188.67,+222.56,+287.21,-180.00,+0.00,-177.84)(7,0)
