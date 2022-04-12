1 Dly 1
2 Servo Off
3 Dly 0.4
4 Dim MDATA(6)
5 M0 = 1
6 *LOOP
7 Open "COM1:" As #1 '
8 Input #1,C1$
9 MDATA(M0)= Val(C1$)
10 M0 = M0+1
11 If M0 > 6 Then GoTo *NMOV
12 Print #1,C1$
13 Close #1
14 GoTo *LOOP
15 '
16 '
17 *NMOV
18 Dim Mworklist(6)
19 Mworklist(1) = MDATA(1)
20 Mworklist(2) = MDATA(2)
21 Mworklist(3) = MDATA(3)
22 Mworklist(4) = MDATA(4)
23 Mworklist(5) = MDATA(5)
24 Mworklist(6) = MDATA(6)
25 '
26 '
27 Dim PKANAP(5)
28 PKANAP(1) = PKANA1
29 PKANAP(2) = PKANA2
30 PKANAP(3) = PKANA3
31 PKANAP(4) = PKANA4
32 PKANAP(5) = PKANA5
33 '
34 '
35 Dim PKANAU(5)
36 PKANAU(1) = pKANA10
37 PKANAU(2) = PKANA20
38 PKANAU(3) = PKANA30
39 PKANAU(4) = PKANA40
40 PKANAU(5) = PKANA50
41 '
42 '-------------Initial Moves & Variable declaration--------------
43 Dly 0.4
44 Servo On
45 Dly 0.7
46 PTPUT=(+823.28,-13.07,+327.82,+178.45,+0.02,-90.00)
47 Def Plt 1, P1,P2,P4,P3,5,2,11
48 Def Plt 2, P1,P2,P4,P3,5,2,11
49 M30 = 1
50 MCOUNT = 0
51 Mov PHOME
52 Dly 0.3
53 HClose 2
54 Dly 0.5
55 HOpen 2
56 Dly 0.3
57 M_Out(6001)= 0' Reset Hex Nut Counter
58 M_Out(6002) = 0'Reset Hex Nut time error
59 M_Out(6003) = 0' Release latches
60 M_Out(6004) = 0 'X104 Belt Conveyer move/stop
61 M_Out(6030) = 0 'to terminate trigger X136
62 M_DOut(6006) = Mworklist(6) ' for the number of hex nuts
63 M6 = Mworklist(6)
64 Dly 0.2
65 M_Out(6030) = 1 ' to trigger hex nut picking X136
66 Dly 0.2
67 M_Out(6030) = 0 ' to terminate trigger X136
68 '---------------------------------------------------------------
69 '
70 '-----------------------Pick Up Box-----------------------------
71 Mov PICK,-100
72 Wait M_In(6007) = 1
73 Mvs PICK
74 Dly 0.5
75 HClose 2
76 Dly 0.7
77 Mvs PICK, -180
78 Mov place, -150
79 Mov place
80 Dly 0.5
81 HOpen 2
82 Dly 0.7
83 Mov place, -150
84 M_Out(6003) = 1 'X103 Activate Blue box latches
85 Mov PTRANSIT'
86 '---------------- --------------- -----------------------------
87 '
88 '------------------------- Work Loop --------------------------
89 M100 = 1
90 For M10 = 1 To 5' 5 means the length of vector mworklist
91     For M20 = 1 To Mworklist(M10)
92         If M100 = 1 And Mworklist(1) > 0 Then
93             GoSub *ROUTINE
94         ElseIf M100 = 2 And Mworklist(2) > 0 Then
95                 GoSub *ROUTINE
96         ElseIf M100 = 3 And Mworklist(3) > 0 Then
97                 GoSub *ROUTINE
98         ElseIf M100 = 4 And Mworklist(4) > 0 Then
99                 GoSub *ROUTINE
100         ElseIf M100 = 5 And Mworklist(5) > 0 Then
101                 GoSub *ROUTINE
102         EndIf
103     Next M20
104     M100 = M100+1
105 '
106 Next M10
107 '----------------- ------------------ ------------------------
108 '
109 '------------- PKANA6 HEX NUTS -----------------
110 If Mworklist(6) >=1 Then
111     PTPUT=(+783.28,-13.07,+327.82,+178.45,+0.02,-90.00)
112     Mov PTRANSIT3
113     Mov PKANA60
114     While (M_DIn(6006) < M6)'the sum allocated = the number of hex nuts counted D1006
115         If M_In(6030) = 1 Then ' No more hex nuts in the tank Y36
116             M_Out(6002) = 1 ' Reset Hex nut errors
117             Dly 0.1
118             M_Out(6002) = 0
119             Print #1,"HNERROR"
120             Input #1, C21$
121             Error 9101'Hex nut Error (for now)
122         EndIf
123         If M_In(6017) = 1 Then' meaning hex nut count is done Y21/ to confirm D1006 or DIn(6006)
124             Print #1, "KANA6"
125             Input #1, C21$
126             Break
127         EndIf
128     WEnd
129     M_Out(6001) = 1
130     Dly 0.1
131     M_Out(6001)= 0
132     HOpen 2
133     Dly 0.7
134     Mvs PKANA6
135     Dly 0.3
136     HClose 2
137     Dly 0.5
138     Mvs P_Curr*(+0.00,+0.00,-30.00,+0.00,+0.00,+0.00)
139     Mvs P_Curr*(+0.00,+60.00,+0.00,+0.00,+0.00,+0.00)
140     Mvs P_Curr*(+0.00,+0.00,-160.00,+0.00,+0.00,+0.00)
141     Cnt 1
142     Mov PPUT*(-80.00,+170.00,-160.00,+0.00,+0.00,+0.00)
143     Mov PPUT*(-80.00,+190.00,-160.00,+0.00,+0.00,+0.00)
144     Mov PPUT*(-40.00,+0.00,+0.00,-81.00,+0.00,-70.00)
145     Dly 1
146     Mov PPUT*(-50.00,+100.00,-160.00,+0.00,+0.00,+0.00)
147     Cnt 0
148     Mov PKANA6*(+0.00,+60.00,-160.00,+0.00,+0.00,+0.00)
149     Mvs P_Curr*(+0.00,+0.00,+130.00,+0.00,+0.00,+0.00)
150     Mov PKANA6,-30
151     Dly 0.2
152     Mvs PKANA6
153     Dly 0.3
154     HOpen 2
155     Dly 0.7
156     Mvs P_Curr*(+0.00,+0.00,-180.00,+0.00,+0.00,+0.00)
157 EndIf
158 '------------------------------------------------------------
159 '
160 '--------------Release Latches and Move Conveyer-------------
161 '
162 M_Out(6003) = 0 'X103 Realease Blue Box latches
163 Dly 1
164 M_Out(6004) =1 'X104 Command to move the belt conveyer
165 Dly 1.5
166 M_Out(6004) = 0 'X104 Command to Stop the belt conveyer,
167 Mov PTRANSIT
168 Print #1,"END"
169 Close #1
170 End
171 '------------------------JOB COMPLETE-------------------------
172 '
173 '--------------------- ROUTINE SUBPROGRAM --------------------
174 *ROUTINE
175 Ovrd 100
176 If M100 = 1 Or M100 = 2 Then GoTo *SPECIALP
177 If M100 = 4 Or M100 = 5 Then Mov PTRANSIT3
178 '
179 Dly 0.5
180 Mov PKANAU(M100)
181 Dly 0.3
182 HOpen 2
183 Dly 0.7
184 If M100 = 3 Then Wait M_In(6019) = 1
185 If M100 = 4 Then Wait M_In(6020) = 1
186 If M100 = 5 Then Wait M_In(6022) = 1
187 Mov PKANAP(M100)
188 Dly 0.3
189 HClose 2
190 Dly 0.5
191 '
192 If M100 = 5 Then
193     Mov P_Curr*(+17.00,+0.00,+0.00,+0.00,+0.00,+0.00)
194     Cnt 1
195     Mov P_Curr*(+0.00,+0.00,-110.00,+0.00,+0.00,+0.00)
196     Mov PKANA51
197     Cnt 0
198 Else
199     Mov P_Curr*(+0.00,-30.00,-13.00,+0.00,+0.00,+0.00)
200     Mov P_Curr*(+0.00,+0.00,-70.00,+0.00,+0.00,+0.00)
201 EndIf
202 Cnt 1
203 Mov PTRANSIT2
204 Mov PPUT,-110
205 Cnt 0
206 '
207 '
208 *COMEBACK
209 '-------------------- For Kanamono E1 -------------------
210 If M100 = 1 Then
211     If M30 > 10 Then
212         GoSub *OVERTENKANA
213         GoTo *PALETSTS4
214     EndIf
215     P100 = Plt 1, M30
216     If M30 >= 6 Then
217         Mov P100*(-13.30,-20.00,+0.00,+0.00,+0.00,+180.00)
218     Else
219         Mov P100
220     EndIf
221     Dly 0.4
222     Mov P_Curr*(+0.00,+0.00,+93.80,+0.00,+0.00,+0.00)
223     Dly 0.3
224     If M30 >= 6 Then Mov P_Curr*(+0.00,-45.00,+0.00,+0.00,+0.00,+0.00)
225     HOpen 2
226     Dly 0.7
227     Mov P_Curr*(+0.00,+0.00,-200.00,+0.00,+0.00,+0.00)
228     GoTo *PALETSTS1
229 EndIf
230 '
231 '----------------------  For Kanamono E2  ---------------------
232 If M100 = 2 Then
233     If M30 > 10 Then
234         GoSub *OVERTENKANA
235         GoTo *PALETSTS3
236     EndIf
237     P200 = Plt 2, M30
238     If M30 >= 6 Then
239         Mov P200*(-20.00,-40.00,-161.90,+0.00,-1.00,+180.00)
240         Dly 0.4
241         Mvs P_Curr*(-2.00,+0.00,+199.00,+0.00,+0.00,+0.00)
242     Else
243         Mov P200*(+22.00,-60.00,-155.30,-10.00,-4.00,+2.00)
244         Dly 0.4
245         Mvs P_Curr*(+6.00,+0.00,+199.00,+0.00,+0.00,+0.00)
246         Dly 1
247     EndIf
248     If M30 >= 6 Then Mov P_Curr*(+2.00,-60.00,+0.00,+0.00,+0.00,+0.00)
249     If M30 = 5 Then
250         HOpen 2
251         Dly 0.3
252         Mvs P_Curr*(+0.00,+0.00,-50.00,+0.00,+0.00,+0.00)
253         Mvs P_Curr*(-7.00,-57.00,+0.00,+0.00,+0.00,+0.00)
254         Mvs P_Curr*(+0.00,+0.00,+50.00,+0.00,+0.00,+0.00)
255         Mvs P_Curr*(+9.00,-21.00,+0.00,+0.00,+0.00,+0.00)
256     Else
257         Dly 0.7
258         HOpen 2
259         Dly 1
260     EndIf
261     Mov P_Curr*(+0.00,+25.00,-199.00,+0.00,+0.00,+0.00)
262     GoTo *PALETSTS2
263 EndIf
264 '-----------------------------------------------------------------
265 '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
266 Ovrd 20
267 If M30 > 6 Then PTPUT=(+863.28,-13.07,+327.82,+178.45,+0.02,-90.00)
268 Mvs PPUT
269 Dly 0.3
270 HOpen 2
271 Dly 0.7
272 Mov P_Curr*(+0.00,+0.00,-100.00,+0.00,+0.00,+0.00)
273 MCOUNT = MCOUNT+1
274 If MCOUNT = 5 And M30 > 10 Then
275     PTPUT=(+823.28,-13.07,+327.82,+178.45,+0.02,-90.00)
276 ElseIf MCOUNT = 5 And M30 <= 10 Then
277     PTPUT=(+863.28,-13.07,+327.82,+178.45,+0.02,-90.00)
278 ElseIf MCOUNT = 10 Then
279     MCOUNT = 0
280     PTPUT=(+823.28,-13.07,+327.82,+178.45,+0.02,-90.00)
281 Else
282     'PPUT = PPUT*(-33.00,+0.00,+0.00,+0.00,+0.00,+0.00)
283     PPUT = PPUT*(-11.00,+0.00,+0.00,+0.00,+0.00,+0.00)
284 EndIf
285 '
286 *JUMP
287 Mov PTRANSIT '
288 If M100 <> 1 And M100 <> 2 Then Mov PTRANSIT
289 Return
290 '--------------  END OF ROUTINE SUBPROGRAM -----------------
291 '----------------- Kanamono E1 & E2 SUBPROGRAM -------------
292 *SPECIALP
293 Mov PKANAU(M100)
294 Dly 0.3
295 HOpen 2
296 Dly 0.7
297 Wait M_In(6023) = 1 ' wait y27 sensor for Kanamono E2
298 Mvs PKANAP(M100)
299 Dly 0.5
300 HClose 2
301 Dly 0.5
302 PTPUT = PPUT*(+0.00,+0.00,-120.00,+0.00,+0.00,+0.00)
303 Cnt 1
304 Mvs PKANAU(M100)
305 If M100 = 2 Then
306     Mov PTPUT*(+0.00,+0.00,-100.00,+0.00,+0.00,+0.00)
307 Else
308     Mov PTPUT
309 EndIf
310 Cnt 0
311 GoTo *COMEBACK
312 '
313 '------------------E1 & E2 Special Positions ---------------------
314 *OVERTENKANA
315 Cnt 1
316 If M30 = 11 Then '
317     Mov PLARGEKANA1,-170
318     Mvs PLARGEKANA1
319     If M100 = 1 Then Mov PSMALLKANA1
320     Dly 0.3
321     HOpen 2
322     Dly 0.7
323     Mvs PLARGEKANA1,-170
324 ElseIf M30 = 12 Then
325     Mov PLARGEKANA2,-170
326     Mvs PLARGEKANA2
327     If M100 = 1 Then Mov PSMALLKANA2
328     Dly 0.2
329     Mov P_Curr*(+0.00,-75.00,+0.00,+0.00,+0.00,+0.00)
330     Dly 0.3
331     HOpen 2
332     Dly 0.7
333     Mvs PLARGEKANA2,-170
334 ElseIf M30 = 13 Then
335     Mov PLARGEKANA3,-170
336     Mvs PLARGEKANA3
337     If M100 = 1 Then Mov PSMALLKANA3
338     Dly 0.3
339     HOpen 2
340     Dly 0.7
341     Mvs PLARGEKANA3,-170
342 ElseIf M30 = 14 Then
343     Mov PLARGEKANA4,-300
344     Mvs PLARGEKANA4
345     If M100 = 1 Then Mov PSMALLKANA4
346     Dly 0.2
347     Mov P_Curr*(+0.00,-50.00,+0.00,+0.00,+0.00,+0.00)
348     Dly 0.3
349     HOpen 2
350     Dly 0.7
351     Mvs PLARGEKANA4,-170
352 Else
353     M30 = 0
354 EndIf
355 Cnt 0
356 Return
357 '----------------- PART OF E1 & E2 SUBPROGRAM--------------------
358 *PALETSTS4
359 *PALETSTS3
360 *PALETSTS1
361 *PALETSTS2
362 If M30 >= 14 Then Mov PTRANSIT
363 M30 = M30+1
364 GoTo *JUMP
365 '----------------------------ERROR--------------------------------
366 *ERRROR
367 'Error 9101 is defined in the settings.
PKANAP(1)=(+470.92,+599.61,+390.01,+177.17,+11.85,-91.98,+0.00,+0.00)(7,0)
PKANAP(2)=(+477.03,+655.14,+581.03,+178.57,+14.94,-90.15,+0.00,+0.00)(7,0)
PKANAP(3)=(+327.99,+469.14,+223.39,-80.31,+6.68,+0.62,+0.00,+0.00)(6,0)
PKANAP(4)=(+103.64,+471.00,+237.66,-84.39,+7.10,-1.46,+0.00,+0.00)(6,0)
PKANAP(5)=(-74.57,+506.50,+278.02,+12.62,-84.88,-104.60,+0.00,+0.00)(6,15728640)
PKANA1=(+470.92,+599.61,+390.01,+177.17,+11.85,-91.98)(7,0)
PKANA2=(+477.03,+655.14,+581.03,+178.57,+14.94,-90.15)(7,0)
PKANA3=(+327.99,+469.14,+223.39,-80.31,+6.68,+0.62)(6,0)
PKANA4=(+103.64,+471.00,+237.66,-84.39,+7.10,-1.46)(6,0)
PKANA5=(-74.57,+506.50,+278.02,+12.62,-84.88,-104.60)(6,15728640)
PKANAU(1)=(+447.55,+559.61,+503.78,+179.66,+16.92,-91.25,+0.00,+0.00)(7,0)
PKANAU(2)=(+448.96,+614.63,+698.32,-169.98,+19.21,-86.97,+0.00,+0.00)(7,0)
PKANAU(3)=(+327.62,+316.10,+190.27,-80.31,+6.68,+0.62,+0.00,+0.00)(6,0)
PKANAU(4)=(+102.92,+362.47,+218.60,-84.42,+7.11,-1.47,+0.00,+0.00)(6,0)
PKANAU(5)=(-61.26,+372.88,+247.43,+12.56,-84.88,-104.54,+0.00,+0.00)(6,15728640)
pKANA10=(+447.55,+559.61,+503.78,+179.66,+16.92,-91.25)(7,0)
PKANA20=(+448.96,+614.63,+698.32,-169.98,+19.21,-86.97)(7,0)
PKANA30=(+327.62,+316.10,+190.27,-80.31,+6.68,+0.62)(6,0)
PKANA40=(+102.92,+362.47,+218.60,-84.42,+7.11,-1.47)(6,0)
PKANA50=(-61.26,+372.88,+247.43,+12.56,-84.88,-104.54)(6,15728640)
PTPUT=(+823.28,-13.07,+327.82,+178.45,+0.02,-90.00)(7,0)
P1=(+788.70,-82.27,+184.92,+178.45,+0.02,-90.00)(7,0)
P2=(+788.70,+116.27,+184.92,+178.45,+0.02,-90.00)(7,0)
P4=(+848.70,+116.27,+184.92,+178.45,+0.02,-90.00)(7,0)
P3=(+848.70,-82.27,+184.92,+178.45,+0.02,-90.00)(7,0)
PHOME=(+251.72,+4.35,+379.47,+176.90,+2.01,-89.86)(7,0)
PICK=(+731.40,-350.33,+122.14,+176.90,+2.01,-89.85)(7,0)
place=(+748.72,+8.11,+137.46,+176.90,+2.01,-89.85)(7,0)
PTRANSIT=(+385.62,+17.44,+433.79,+178.45,+0.02,-86.19)(7,0)
PTRANSIT3=(+56.72,+307.87,+433.79,+178.45,+0.02,-7.23)(7,0)
PKANA60=(+103.07,+452.18,+234.08,-177.86,+1.31,+0.00)(7,0)
PKANA6=(+103.07,+452.18,+71.31,-177.86,+1.31,+0.00)(7,0)
PPUT=(+827.04,-13.07,+207.82,+178.45,+0.02,-90.00)(7,0)
PKANA51=(+216.29,+326.48,+330.74,-9.44,-79.41,-125.13)(6,15728640)
PTRANSIT2=(+468.44,+4.66,+306.79,+178.45,+0.02,-86.19)(7,0)
P100=(+687.50,-181.06,+279.70,+178.45,+0.02,-90.00,+0.00,+0.00)(7,0)
P200=(+687.50,-81.93,+279.70,+178.45,+0.02,-90.00,+0.00,+0.00)(7,0)
PLARGEKANA1=(+720.58,-204.19,+239.21,+178.45,+0.02,+0.00)(7,15728640)
PSMALLKANA1=(+732.03,-205.62,+186.25,-179.35,+2.27,-0.02)(7,15728640)
PLARGEKANA2=(+709.23,-92.64,+239.98,-179.28,-0.15,-180.00)(7,0)
PSMALLKANA2=(+721.11,-90.95,+186.13,-179.85,-4.10,+179.88)(7,0)
PLARGEKANA3=(+722.77,-124.34,+239.93,+178.81,-0.22,+0.02)(7,15728640)
PSMALLKANA3=(+728.18,-119.63,+184.20,+178.45,+0.02,+0.00)(7,15728640)
PLARGEKANA4=(+706.42,-23.55,+242.74,+178.45,+0.20,-179.98)(7,0)
PSMALLKANA4=(+716.46,-31.69,+188.45,+178.45,+0.02,+180.00)(7,0)
PSHOME=(+613.74,+5.87,+394.66,+177.86,+0.77,-89.89)(7,0)
