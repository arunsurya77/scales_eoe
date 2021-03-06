#AA$ = "C:\Users\Arun\Documents\ka.txt"
#GETTEXTFILE AA$, POP    # Import POP text data file
DECLARE x,double,1,18
DECLARE y,double,1,18
pref$ = "C:\Users\aruns\Documents\scales_field\"
FOR c,1,18,1

SETCONFIG c
x_$ = pref$+$STR(c)+"_x.txt"
OPEN x_$
FOR z,1,18,1
READNEXT x1
x(z)=x1
#PRINT x(z)
NEXT z
CLOSE

y_$ = pref$+$STR(c)+"_y.txt"
OPEN y_$
FOR z,1,18,1
READNEXT y1
y(z)=y1
#PRINT y(z)
NEXT z
CLOSE


FOR z,1,18,1
SYSP 100, 1
SYSP 101, 1
PRINT z
SYSP 102, 1, x(z)
#PRINT x(z)
#PRINT y(z)
SYSP 103, 1, y(z)
SYSP 104, 1, 1

SYSP 201, 1  # set total wavelength number as 1
filename$ = "C:\Users\aruns\Documents\slenslet\K_pdr\ls"
start_value =1.95#2.9000#1.95# 4.5000#1.95 #1.5965
stop_value = 2.45#4.1500#2.45# 5.2000#1.6783
increment = (stop_value-start_value)/4 #0.01
FOR i, start_value, stop_value, increment
   SYSP 202, 1, i
   SYSP 200, 1 # set the 2nd wavelength as the primary wavelength
   #A$ = $TEMPFILENAME()
   
   A$ = filename$ +"_"+$STR(c)+"_"+$STR(z)+"_"+$STR(i) +".dat"
   
   GETTEXTFILE A$, Spt   
   
   #filewrite
   #OPEN A$
   #LABEL 1
   #READSTRING B$
   #IF (!EOFF())
    # OUTPUT outputfile$, APPEND
    # PRINT B$
    # GOTO 1
   #ENDIF
   #CLOSE   
   #end filewrite
   
NEXT i
NEXT z
PRINT c
NEXT c