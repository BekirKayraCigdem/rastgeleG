from email import charset
import random

birKelime=[]
ikiKelime=[]
ucKelime=[]
dortKelime=[]
besKelime=[]
altiKelime=[]
yediKelime=[]
sekizKelime=[]

secim = int(input("(Seç 2/3/4/5/6/7/8):"))

for line in open("randomLine1.txt").readlines():
    line_1 =line.strip()
    birKelime.append(line_1)

for line in open("randomLine2.txt").readlines():
    line_2= line.strip()
    ikiKelime.append(line_2)

for line in open("randomLine3.txt").readlines():
    line_3= line.strip()
    ucKelime.append(line_3)

for line in open("randomLine4.txt").readlines():
    line_4= line.strip()
    dortKelime.append(line_4)

for line in open("randomLine5.txt").readlines():
    line_5= line.strip()
    besKelime.append(line_5)

for line in open("randomLine6.txt").readlines():
    line_6= line.strip()
    altiKelime.append(line_6)

for line in open("randomLine7.txt").readlines():
    line_7= line.strip()
    yediKelime.append(line_7)

for line in open("randomLine8.txt").readlines():
    line_8= line.strip()
    sekizKelime.append(line_8)



cikti = open("cikti.txt","w")

l= 0

random.shuffle(birKelime)
random.shuffle(ikiKelime)
random.shuffle(ucKelime)
random.shuffle(dortKelime)
random.shuffle(besKelime)
random.shuffle(altiKelime)
random.shuffle(yediKelime)
random.shuffle(sekizKelime)

if secim ==2 :

    for birK in birKelime:
        for ikiK in ikiKelime:
            cikti.write(birK+" "+ikiK)
            l+=1
            if l == 1 :
                 l = 0
                 cikti.write("\n")  

elif secim ==3 :

    for birK in birKelime:
        for ikiK in ikiKelime:  
            for ucK in ucKelime:
                cikti.write(birK+" "+ikiK+" "+ucK)
                l+=1
                if l == 1 :
                     l = 0
                     cikti.write("\n") 

elif secim ==4 :

    for birK in birKelime:
        for ikiK in ikiKelime:  
            for ucK in ucKelime:
                for dortK in dortKelime:
                    cikti.write(birK+" "+ikiK+" "+ucK+" "+dortK)
                    l+=1
                    if l == 1 :
                         l = 0
                         cikti.write("\n") 

elif secim ==5 :

    for birK in birKelime:
        for ikiK in ikiKelime:  
            for ucK in ucKelime:
                for dortK in dortKelime:
                    for besK in besKelime:
                        cikti.write(birK+" "+ikiK+" "+ucK+" "+dortK+" "+besK)
                        l+=1
                        if l == 1 :
                             l = 0
                             cikti.write("\n") 

elif secim ==6 :

    for birK in birKelime:
        for ikiK in ikiKelime:  
            for ucK in ucKelime:
                for dortK in dortKelime:
                    for besK in besKelime:
                        for altiK in altiKelime:
                            cikti.write(birK+" "+ikiK+" "+ucK+" "+dortK+" "+besK+" "+altiK)
                            l+=1
                            if l == 1 :
                                 l = 0
                                 cikti.write("\n") 

elif secim ==7 :

    for birK in birKelime:
        for ikiK in ikiKelime:  
            for ucK in ucKelime:
                for dortK in dortKelime:
                    for besK in besKelime:
                        for altiK in altiKelime:
                            for yediK in yediKelime:
                                cikti.write(birK+" "+ikiK+" "+ucK+" "+dortK+" "+besK+" "+altiK+" "+yediK)
                                l+=1
                                if l == 1 :
                                     l = 0
                                     cikti.write("\n") 

elif secim == 8 :

    for birK in birKelime:
        for ikiK in ikiKelime:  
            for ucK in ucKelime:
                for dortK in dortKelime:
                    for besK in besKelime:
                        for altiK in altiKelime:
                            for yediK in yediKelime:
                                for sekizk in sekizKelime:
                                    cikti.write(birK+" "+ikiK+" "+ucK+" "+dortK+" "+besK+" "+altiK+" "+yediK+" "+sekizk)
                                    l+=1
                                    if l == 1 :
                                         l = 0
                                         cikti.write("\n") 

else :
    print("Geçersiz giriş.")