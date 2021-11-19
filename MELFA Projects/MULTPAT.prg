1 ' Define the necessary variables both local and public
2 '--------------------------------Part 1 -------------------------------------
3 Def Pos P_CMTL ' Hand camera: Camera center position data
4 Def Pos P_CLPos ' Hand camera: Reference point to start calibration
5 Def Pos P_CMH ' Hand camera: Offset from the surface of the identified workpiece to the imaging point
6 Def Pos P_HVSP1 ' Hand camera: Default imaging point
7 Def Pos P_WRK03 ' Hand camera: Master workpiece grasp position
8 Def Pos P_PVS03 ' Hand camera: Master workpiece identification point
9 Def Pos P_PH03 ' Hand camera: Coefficient for calculating the handling position from the position of the identified workpiece
10 Def Char C_C03 ' Hand camera: COM name
11 Def Char C_J03 ' Hand camera: Job name
12 Def Pos P_PHome ' Safe position
13 Loadset 1,1
14 OAdl On
15 Servo On
16 Wait M_Svo=1
17 '-----------------------------------------------------------------------------------------------------
18 '
19 'Read text file and take both string and integer data
20 '------------------------------------Part 2 -----------------------------------------------------------
21 Open "kanafile.txt" For Input As #1
22 Input #1, C1$
23 Input #1, M1
24 Input #1, C2$
25 Input #1, M2
26 Input #1, C3$
27 Input #1, M3
28 Input #1, C4$
29 Input #1, M4
30 Close #1
31 Dly 0.2
32 '
33 '-------------------------------------------------------------------------------------------------
34 'Define the palette for search area
35 '-----------------------------------------Part 3 ^------------------------------------------------
36 M55 = 1 'Counter for palette position
37 M50 = 5 'Pallete x
38 M51 = 10 'Palette y
39 M52 = M50*M51 ' Palette total num of stops
40 Def Plt 1,P31,P32,P33,P34,M50,M51,11
41 '------------------------------------------------------------------------------------------------
42 '
43 Mov P_PHome
44 '-----------------Hand INIT-----------
45 Dly 1
46 HClose 1
47 Dly 2
48 HOpen 1
49 Dly 0.3
50 '---------------------****---------------------------
51 *LOOP
52 P100 = Plt 1,M55
53 GoSub *VISION
54 GoSub *PICK
55 GoSub *PLACE
56 *MLP
57 M55 = M55+1
58 If M55 <= M52 Then *LOOP
59 Mov P_PHome
60 Hlt
61 End
62 '---------------------****---------------------------
63 '
64 *VISION
65 Tool P_NTool
66 MCNT=1
67 HOpen 1
68 M_Out(10129)=0
69 M_Out(10128)=1 Dly 0.1
70 Dly 0.5
71 If M_NvOpen(1)<>1 Then
72 NVOpen C_C03$ As #1
73 Wait M_NvOpen(1)=1
74 EndIf
75 NVLoad #1, "Allan"
76 Dly 0.3
77 Mov P100
78 Dly 1
79 *RETRY
80 NVRun #1, "Allan"
81 EBRead #1,,MNUM1,PVS1,CID1$,MNUM2,PVS2,CID2$,MNUM3,PVS3,CID3$,MNUM4,PVS4,CID4$
82 Dly 0.1
83 MID0 = 0
84 MID1 = Val(CID1$)
85 MID2 = Val(CID2$)
86 MID3 = Val(CID3$)
87 MID4 = Val(CID4$)
88 If MNUM1 = 1 Then
89     If M1 > 0 Then
90         MNUM = MNUM1
91         PVS = PVS1
92         MID0 = MID1
93         M1 = M1-1
94         Break
95     Else
96         GoTo *MLP
97     EndIf
98 ElseIf MNUM2 = 1 Then
99     If M2 > 0 Then
100         MNUM = MNUM2
101         PVS = PVS2
102         MID0 = MID2
103         M2= M2=1
104         Break
105     Else
106         GoTo *MLP
107     EndIf
108 ElseIf MNUM3 = 1 Then
109     If M3 > 0 Then
110         MNUM = MUM3
111         PVS = PVS3
112         MID0 = MID3
113         M3 = M3-1
114         Break
115     Else
116         GoTo *MLP
117     EndIf
118 ElseIf MNUM4 = 1 Then
119     If M4 > 0 Then
120         MNUM = MUM4
121         PVS = PVS4
122         MID0 = MID4
123         M4 = M4-1
124         Break
125     Else
126         GoTo *MLP
127     EndIf
128 EndIf
129 '=--------=---------=----------=----------=---------=---------=----------=----------=--------=
130 Dly 0.1
131 If MNUM>=1 Then *OK
132 MCNT=MCNT+1
133 If MCNT>2 Then 'Didn't find any object after 2 loops
134     GoTo *MLP' Move to next palette
135 EndIf
136 Dly 0.2
137 GoTo *RETRY
138 *OK
139 MCNT=1
140 PTRG=P100*P_CMTL*PVS*P_PH03 'PTRG=P_HVSP1*P_CMTL*PVS*P_PH03
141 Return
142 '---------------------****---------------------------
143 *PICK
144 Mov PTRG,-100
145 Dly 0.5
146 HOpen 1
147 Dly 0.5
148 Mvs PTRG,20
149 Dly 0.6
150 HClose 1
151 Dly 0.5
152 Mvs PTRG,-100
153 Dly 0.1
154 Return
155 '---------------------****---------------------------
156 '
157 *PLACE
158 If MID0 = 1 Then PPUT = P1
159 If MID0 = 2 Then PPUT = P2
160 If MID0 = 3 Then PPUT = P3
161 If MID0 = 4 Then PPUT = P4
162 Mov PPUT, -100
163 Mvs PPUT
164 HOpen 1
165 Dly 0.5
166 Mvs PPUT,-100
167 GoTo *MLP
168 Return
P_CMTL=(0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00)(,)
P_CLPos=(0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00)(,)
P_CMH=(0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00)(,)
P_HVSP1=(0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00)(,)
P_WRK03=(0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00)(,)
P_PVS03=(0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00)(,)
P_PH03=(0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00)(,)
P_PHome=(0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00)(,)
P31=(+399.76,-256.14,+506.91,+180.00,+0.00,+175.90)(7,0)
P32=(+636.85,-256.14,+506.91,+180.00,+0.00,+175.90)(7,0)
P33=(+636.85,+255.20,+506.91,+180.00,+0.00,+175.90)(7,0)
P34=(+399.76,+255.20,+506.91,-180.00,+0.00,+175.90)(7,0)
P100=(+0.00,+0.00,+0.00,+0.00,+0.00,+0.00,+0.00,+0.00)(,)
PVS1=(+0.00,+0.00,+0.00,+0.00,+0.00,+0.00,+0.00,+0.00)(,)
PVS2=(+0.00,+0.00,+0.00,+0.00,+0.00,+0.00,+0.00,+0.00)(,)
PVS3=(+0.00,+0.00,+0.00,+0.00,+0.00,+0.00,+0.00,+0.00)(,)
PVS4=(+0.00,+0.00,+0.00,+0.00,+0.00,+0.00,+0.00,+0.00)(,)
PVS=(+16.24,+2.82,+0.00,+0.00,+0.00,-3.36,+0.00,+0.00)(0,0)
PTRG=(+402.83,-13.26,+198.57,+180.00,+0.00,+179.26,+0.00,+0.00)(7,0)
PPUT=(+188.67,+222.56,+287.21,-180.00,+0.00,-177.84)(7,0)
P1=(+500.10,-0.00,+538.21,+180.00,-0.10,-179.52)(7,0)
P2=(+500.10,-0.00,+538.21,+180.00,-0.10,-179.52)(7,0)
P3=(+500.10,-0.00,+538.21,+180.00,-0.10,-179.52)(7,0)
P4=(+500.10,-0.00,+538.21,+180.00,-0.10,-179.52)(7,0)
P200=(+0.00,+0.00,+0.00,+0.00,+0.00,+0.00,+0.00,+0.00)(,)
P8th=(+0.00,+0.00,+0.00,+0.00,+0.00,+0.00,+0.00,+0.00)(,)
