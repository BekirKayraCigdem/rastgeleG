import random

r = []

for line in open("cikti.txt").readlines():
    line_1= line.strip()
    r.append(line_1)

sonuc = open("sonuc.txt","w")

i = 0

random.shuffle(r)

for m in r :
    sonuc.write(m)
    i+=1
    if i == 1:
        i = 0
        sonuc.write("\n")