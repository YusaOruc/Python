turkd=float(raw_input("T�rk�e do�ru say�n�z� giriniz:"))
turky=float(raw_input("T�rk�e yanl�� say�n�z� giriniz:"))
Turkss=turkd+turky
if Turkss<=40:
   TNS=turkd-(turky/4)
   print "TNS",TNS
else:
       print"Ge�ersiz soru say�s� girdiniz"
      



matd=float(raw_input("Matematik do�ru say�n�z� giriniz:"))
maty=float(raw_input("Matematik yanl�� say�n�z� giriniz:"))
Matss=matd+maty
if Matss<=40:
   MNS=matd-(maty/4)
   print "MNS",MNS
else:
       print"Ge�ersiz soru say�s� girdiniz"



sosd=float(raw_input("Sosyal do�ru say�n�z� giriniz:"))
sosy=float(raw_input("Sosyal yanl�� say�n�z� giriniz:"))
Sosss=sosd+sosy
if Sosss<=40:
   SNS=sosd-(sosy/4)
   print "SNS",SNS
else:
       print"Ge�ersiz soru say�s� girdiniz"



fend=float(raw_input("Fen do�ru say�n�z� giriniz:"))
feny=float(raw_input("Fen yanl�� say�n�z� giriniz:"))
Fenss=fend+feny
if Fenss<=40:
   FNS=fend-(feny/4)
   print "FNS",FNS
else:
       print"Ge�ersiz soru say�s� girdiniz"

if Turkss<=40 and Matss<=40 and Sosss<=40 and Fenss<=40:
    TP=TNS*4
    MP=MNS*3
    SP=SNS*2
    FP=FNS*1
    YGSPUAN=TP+MP+SP+FP+100
    print "YGSPUAN:",YGSPUAN
else:
    print "Girdi�iniz soru say�lar�n� kontrol ediniz"



EDS=float(raw_input("Edebiyat do�ru say�n�z� giriniz:"))
EYS=float(raw_input("Edebiyat yanl�� say�n�z� giriniz:"))
EDEBIYATSS=EDS+EYS
if EDEBIYATSS<=56:
   ENS=EDS-(EYS/4)
   print "ENS",ENS
else:
       print"Ge�ersiz soru say�s� girdiniz"


MATD=float(raw_input("Matematik lys do�ru say�n�z� giriniz:"))
MATY=float(raw_input("Matemetik lys yanl�� say�n�z� giriniz:"))
MATEMATIKSS=MATD+MATY
if MATEMATIKSS<=80:
   MLNS=MATD-(MATY/4)
   print "MLNS",MLNS
else:
       print"Ge�ersiz soru say�s� girdiniz"



COGD=float(raw_input("Co�rafya do�ru say�n�z� giriniz:"))
COGY=float(raw_input("Co�rafya yanl�� say�n�z� giriniz:"))
COGSS=COGD+COGY
if COGSS<=24:
   CNS=COGD-(COGY/4)
   print "CNS",CNS
else:
       print"Ge�ersiz soru say�s� girdiniz"

if ENS<=56 and MLNS<=80 and CNS<=24:
    ELP=float(ENS*4)
    MLP=float(MLNS*3)
    CLP=float(CNS*1.5)
    LYS=ELP+MLP+CLP
    print "LYS",LYS
else:
    print "Ge�ersiz soru say�s� girdiniz"

LO=float(raw_input("Lise puan ortalaman�z� giriniz:"))

OBP=(LO*60)/100
YP=((YGSPUAN*40)/100)+((LYS*60)/100)+OBP
print"YP",YP
    













































    

