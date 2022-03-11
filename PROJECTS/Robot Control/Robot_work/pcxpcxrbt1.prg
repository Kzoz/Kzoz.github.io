1 'Servo On
2 'Mov PHOME
3 'Mov PLARGEKANA3
4 'Hlt
5 'HOpen 2
6 'Mov PKANA20
7 'Dly 1
8 'Mvs PKANA2
9 'Dly 1
10 'HClose 2
11 'Dly 1
12 'Mvs PKANA20
13 'Dly 1
14 'HClose 2
15 'Def Plt 2, P1,P2,P4,P3,5,2,11
16 'P200 = Plt 2,5
17 ''Mov P200*(-14.00,-40.00,-160.90,+0.00,-1.00,+180.00)
18 'Mov P200*(+22.00,-60.00,-155.30,-10.00,-4.00,+2.00)
19 'Dly 0.4
20 'Mvs P_Curr*(+6.00,+0.00,+199.00,+0.00,+0.00,+0.00)
21 'Dly 3
22 'HOpen 2
23 'Dly 0.5
24 'Mvs P_Curr*(0.00,0.00,-50.00,+0.00,+0.00,+0.00)
25 'Mvs P_Curr*(0.00,-57.00,+0.00,+0.00,+0.00,+0.00)
26 'Mvs P_Curr*(+0.00,0.00,+50.00,+0.00,+0.00,+0.00)
27 'Mvs P_Curr*(+4.00,-21.00,+0.00,+0.00,+0.00,+0.00)
28 'Dly 0.3
29 'Mov P_Curr*(+0.00,-60.00,+0.00,+0.00,+0.00,+0.00)
30 'Dly 0.3
31 'HOpen 2
32 'Dly 1
33 'Mov P_Curr*(+0.00,+25.00,-199.00,+0.00,+0.00,+0.00)
34 'Hlt
35 Dly 1
36 Servo Off
37 Dly 0.4
38 Dim MDATA(6)
39 M0 = 1
40 *LOOP
41 Open "COM1:" As #1 '
42 Input #1,C1$
43 MDATA(M0)= Val(C1$)
44 M0 = M0+1
45 If M0 > 6 Then GoTo *NMOV
46 Print #1,C1$
47 Close #1
48 GoTo *LOOP
49 '
50 '
51 *NMOV
52 Dly 0.4
53 Servo On
54 Dly 0.7
55 PPUT=(+667.10,-177.73,+295.88,+178.45,+0.02,-86.19)
56 Def Plt 1, P1,P2,P4,P3,5,2,11
57 Def Plt 2, P1,P2,P4,P3,5,2,11
58 M30 = 1
59 MCOUNT = 0
60 Mov PHOME
61 Dly 0.3
62 HClose 2
63 Dly 0.5
64 HOpen 2
65 Dly 0.3
66 M_Out(6001)= 0
67 Dly 0.2
68 '
69 '
70 Dim Mworklist(6)
71 Mworklist(1) = MDATA(1)
72 Mworklist(2) = MDATA(2)
73 Mworklist(3) = MDATA(3)
74 Mworklist(4) = MDATA(4)
75 Mworklist(5) = MDATA(5)
76 Mworklist(6) = MDATA(6)
77 '
78 M_DOut(6006) = Mworklist(6) ' for the number of hex nuts
79 M6 = Mworklist(6)
80 Dly 0.2
81 M_Out(6030) = 1 ' to trigger hex nut picking X136
82 Dly 0.2
83 M_Out(6030) = 0 ' to terminate trigger X136
84 '
85 Dim PKANAP(5)
86 PKANAP(1) = PKANA1
87 PKANAP(2) = PKANA2
88 PKANAP(3) = PKANA3
89 PKANAP(4) = PKANA4
90 PKANAP(5) = PKANA5
91 '
92 '
93 Dim PKANAU(5)
94 PKANAU(1) = pKANA10
95 PKANAU(2) = PKANA20
96 PKANAU(3) = PKANA30
97 PKANAU(4) = PKANA40
98 PKANAU(5) = PKANA50
99 '
100 '
101 M100 = 1
102 For M10 = 1 To 5' 5 means the length of vector mworklist
103     For M20 = 1 To Mworklist(M10)
104         If M100 = 1 And Mworklist(1) > 0 Then
105             GoSub *ROUTINE
106         ElseIf M100 = 2 And Mworklist(2) > 0 Then
107                 GoSub *ROUTINE
108         ElseIf M100 = 3 And Mworklist(3) > 0 Then
109                 GoSub *ROUTINE
110         ElseIf M100 = 4 And Mworklist(4) > 0 Then
111                 GoSub *ROUTINE
112         ElseIf M100 = 5 And Mworklist(5) > 0 Then
113                 GoSub *ROUTINE
114         EndIf
115     Next M20
116     M100 = M100+1
117 '
118 Next M10
119 '------------- PKANA6 HEX NUTS -----------------
120 If Mworklist(6) >=1 Then
121     PPUT=(+627.10,-177.73,+265.88,+178.45,+0.02,-86.19)
122     Mov PTRANSIT3
123     Mov PKANA60
124     While (M_DIn(6006) < M6)'the sum allocated = the number of hex nuts counted D1006
125         If M_In(6030) = 1 Then ' No more hex nuts in the tank Y36
126             M_Out(6002) = 1 ' Reset Hex nut errors
127             Dly 0.1
128             M_Out(6002) = 0
129             GoTo *ERRROR
130         EndIf
131         'If M_In(6013) = 1 Then' meaning hex nut count is done Y15/ to confirm D1006 or DIn(6006)
132         If M_In(6017) = 1 Then' meaning hex nut count is done Y21/ to confirm D1006 or DIn(6006)
133             Break
134         EndIf
135     WEnd
136     M_Out(6001) = 1
137     Dly 0.1
138     M_Out(6001)= 0
139     HOpen 2
140     Dly 0.7
141     Mvs PKANA6
142     Dly 0.3
143     HClose 2
144     Dly 0.5
145     Mvs P_Curr*(+0.00,+0.00,-30.00,+0.00,+0.00,+0.00)
146     Mvs P_Curr*(+0.00,+60.00,+0.00,+0.00,+0.00,+0.00)
147     Mvs P_Curr*(+0.00,+0.00,-160.00,+0.00,+0.00,+0.00)
148     Mov PPUT*(+0.00,+0.00,-160.00,+0.00,+0.00,+0.00)
149     Mov PPUT*(-40.00,-50.00,-100.00,-75.00,+0.00,-70.00)
150     Dly 1
151     Mov PPUT*(+0.00,+0.00,-160.00,+0.00,+0.00,+0.00)
152     Mov PKANA6*(+0.00,+60.00,-160.00,+0.00,+0.00,+0.00)
153     Mvs P_Curr*(+0.00,+0.00,+130.00,+0.00,+0.00,+0.00)
154     Mov PKANA6,-30
155     Dly 0.2
156     Mvs PKANA6
157     Dly 0.3
158     HOpen 2
159     Dly 0.7
160     Mvs P_Curr*(+0.00,+0.00,-180.00,+0.00,+0.00,+0.00)
161 EndIf
162 '--------------------------------------
163 Mov PHOME
164 Print #1,"END"
165 Close #1 ' not optimal
166 End
167 '-------------------------------------------------------------------------
168 *ROUTINE
169 Ovrd 100
170 If M100 = 1 Or M100 = 2 Then GoTo *SPECIALP'***
171 If M100 = 4 Or M100 = 5 Then Mov PTRANSIT3
172 '
173 Dly 0.5
174 Mov PKANAU(M100)
175 Dly 0.3
176 HOpen 2
177 Dly 0.7
178 If M100 = 3 Then Wait M_In(6019) = 1
179 If M100 = 4 Then Wait M_In(6020) = 1
180 If M100 = 5 Then Wait M_In(6022) = 1
181 Mov PKANAP(M100)
182 Dly 0.3
183 HClose 2
184 Dly 0.5
185 '
186 If M100 = 5 Then '***
187     Mov P_Curr*(+17.00,+0.00,+0.00,+0.00,+0.00,+0.00)
188     Cnt 1
189     Mov P_Curr*(+0.00,+0.00,-110.00,+0.00,+0.00,+0.00)
190     Mov PKANA51'***
191     Cnt 0
192 Else
193     Mov P_Curr*(+0.00,-30.00,-13.00,+0.00,+0.00,+0.00)
194     Mov P_Curr*(+0.00,+0.00,-70.00,+0.00,+0.00,+0.00)
195 EndIf
196 Cnt 1
197 Mov PTRANSIT2
198 Mov PPUT,-110
199 Cnt 0
200 '
201 '
202 *COMEBACK
203 '----------------- For smaller Kanamono Palette --------------
204 If M100 = 1 Then
205     P100 = Plt 1, M30
206     If M30 >= 6 Then
207         Mov P100*(-13.30,-20.00,+0.00,+0.00,+0.00,+180.00)
208     Else
209         Mov P100
210     EndIf
211     Dly 0.4
212     Mov P_Curr*(+0.00,+0.00,+93.80,+0.00,+0.00,+0.00)
213     Dly 0.3
214     If M30 >= 6 Then Mov P_Curr*(+0.00,-45.00,+0.00,+0.00,+0.00,+0.00)
215     HOpen 2
216     Dly 0.7
217     Mov P_Curr*(+0.00,+0.00,-200.00,+0.00,+0.00,+0.00)
218     GoTo *PALETSTS1
219 EndIf
220 '
221 '----------------- For Bigger Kanamono Palette ---------------------
222 If M100 = 2 Then
223     If M30 > 10 Then
224         GoSub *OVERTENKANA
225         GoTo *PALETSTS3
226     EndIf
227     P200 = Plt 2, M30
228     If M30 >= 6 Then
229         Mov P200*(-20.00,-40.00,-161.90,+0.00,-1.00,+180.00)
230         Dly 0.4
231         Mvs P_Curr*(-2.00,+0.00,+199.00,+0.00,+0.00,+0.00)
232     Else
233         Mov P200*(+22.00,-60.00,-155.30,-10.00,-4.00,+2.00)
234         Dly 0.4
235         Mvs P_Curr*(+6.00,+0.00,+199.00,+0.00,+0.00,+0.00)
236         Dly 1
237     EndIf
238     If M30 >= 6 Then Mov P_Curr*(+2.00,-60.00,+0.00,+0.00,+0.00,+0.00)' x from -6 to -2
239     If M30 = 5 Then
240         HOpen 2
241         Dly 0.3
242         Mvs P_Curr*(+0.00,+0.00,-50.00,+0.00,+0.00,+0.00)
243         Mvs P_Curr*(-7.00,-57.00,+0.00,+0.00,+0.00,+0.00)
244         Mvs P_Curr*(+0.00,+0.00,+50.00,+0.00,+0.00,+0.00)
245         Mvs P_Curr*(+10.00,-21.00,+0.00,+0.00,+0.00,+0.00)
246     Else
247         Dly 0.7
248         HOpen 2
249         Dly 1
250     EndIf
251     Mov P_Curr*(+0.00,+25.00,-199.00,+0.00,+0.00,+0.00)
252     GoTo *PALETSTS2
253 EndIf
254 '--------------------------
255 Ovrd 20
256 Mvs PPUT
257 Dly 0.3
258 HOpen 2
259 Dly 0.7
260 Mov P_Curr*(+0.00,+0.00,-100.00,+0.00,+0.00,+0.00)
261 MCOUNT = MCOUNT+1
262 If MCOUNT = 5 And M30 > 10 Then
263     PPUT=(+667.10,-177.73,+295.88,+178.45,+0.02,-86.19)
264 ElseIf MCOUNT = 5 And M30 <= 10 Then
265     PPUT=(+707.10,-177.73,+295.88,+178.45,+0.02,-86.19)
266 ElseIf MCOUNT = 10 Then
267     MCOUNT = 0
268     PPUT=(+667.10,-177.73,+295.88,+178.45,+0.02,-86.19)
269 Else
270     PPUT = PPUT*(-33.00,+0.00,+0.00,+0.00,+0.00,+0.00)
271 EndIf
272 '
273 *JUMP
274 If M100 <> 1 And M100 <> 2 Then Mov PTRANSIT
275 Return
276 '
277 *SPECIALP
278 Mov PKANAU(M100)
279 Dly 0.3
280 HOpen 2
281 Dly 0.7
282 Wait M_In(6023) = 1 ' wait y27 is ON
283 Mvs PKANAP(M100)
284 Dly 0.5
285 HClose 2
286 Dly 0.5
287 PTPUT = PPUT*(+0.00,+0.00,-120.00,+0.00,+0.00,+0.00)
288 Cnt 1
289 Mvs PKANAU(M100)
290 If M100 = 2 Then
291     Mov PTPUT*(+0.00,+0.00,-100.00,+0.00,+0.00,+0.00)
292 Else
293     Mov PTPUT
294 EndIf
295 Cnt 0
296 GoTo *COMEBACK
297 '
298 '--------------------------------------------------------
299 *OVERTENKANA
300 If M30 = 11 Then '
301     Mov PLARGEKANA1,-170
302     Mvs PLARGEKANA1
303     Dly 0.3
304     HOpen 2
305     Dly 0.7
306     Mvs PLARGEKANA1,-170
307 ElseIf M30 = 12 Then
308     Mov PLARGEKANA2,-170
309     Mvs PLARGEKANA2
310     Dly 0.2
311     Mov P_Curr*(+0.00,-75.00,+0.00,+0.00,+0.00,+0.00)
312     Dly 0.3
313     HOpen 2
314     Dly 0.7
315     Mvs PLARGEKANA2,-170
316 ElseIf M30 = 13 Then
317     Mov PLARGEKANA3,-170
318     Mvs PLARGEKANA3
319     Dly 0.3
320     HOpen 2
321     Dly 0.7
322     Mvs PLARGEKANA3,-170
323 ElseIf M30 = 14 Then
324     Mov PLARGEKANA4,-300
325     Mvs PLARGEKANA4
326     Dly 0.2
327     Mov P_Curr*(+0.00,-50.00,+0.00,+0.00,+0.00,+0.00)
328     Dly 0.3
329     HOpen 2
330     Dly 0.7
331     Mvs PLARGEKANA4,-170
332 Else
333     M30 = 0
334 EndIf
335 Return
336 '-------------------------------------
337 *PALETSTS3
338 *PALETSTS1
339 *PALETSTS2
340 If M30 >= 14 Then Mov PTRANSIT
341 M30 = M30+1
342 GoTo *JUMP
343 '--------------------------------------
344 *ERRROR
345 Error 9100'Hex nut Error
PPUT=(+667.10,-177.73,+295.88,+178.45,+0.02,-86.19)(,)
P1=(+627.47,-230.63,+279.70,+178.45,+0.02,-90.00)(7,0)
P2=(+627.47,-32.36,+279.70,+178.45,+0.02,-90.00)(7,0)
P4=(+687.50,-32.36,+279.70,+178.45,+0.02,-90.00)(7,0)
P3=(+687.50,-230.63,+279.70,+178.45,+0.02,-90.00)(7,0)
PHOME=(+251.72,+4.35,+379.47,+176.90,+2.01,-89.86)(7,0)
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
PTRANSIT3=(+56.72,+307.87,+433.79,+178.45,+0.02,-7.23)(7,0)
PKANA60=(+103.07,+452.18,+234.08,-177.86,+1.31,+0.00)(7,0)
PKANA6=(+103.07,+452.18,+71.31,-177.86,+1.31,+0.00)(7,0)
PKANA51=(+216.29,+326.48,+330.74,-9.44,-79.41,-125.13)(6,15728640)
PTRANSIT2=(+465.97,-81.88,+438.88,-178.71,-0.20,+158.58)(7,0)
P100=(+687.50,-181.06,+279.70,+178.45,+0.02,-90.00,+0.00,+0.00)(7,0)
P200=(+687.50,-81.93,+279.70,+178.45,+0.02,-90.00,+0.00,+0.00)(7,0)
PTRANSIT=(+385.62,+17.44,+433.79,+178.45,+0.02,-86.19)(7,0)
PTPUT=(+670.34,-177.56,+415.84,+178.45,+0.02,-86.19,+0.00,+0.00)(7,0)
PLARGEKANA1=(+720.58,-204.19,+239.21,+178.45,+0.02,+0.00)(7,15728640)
PLARGEKANA2=(+709.23,-92.64,+239.98,-179.28,-0.15,-180.00)(7,0)
PLARGEKANA3=(+722.77,-124.34,+239.93,+178.81,-0.22,+0.02)(7,15728640)
PLARGEKANA4=(+706.42,-23.55,+242.74,+178.45,+0.20,-179.98)(7,0)
