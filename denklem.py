a=int(raw_input("bir k�k girin"))
b=int(raw_input("bir k�k girin"))
c=int(raw_input("bir k�k girin"))
D=b*b-4*a*c
if D<0:
 print "k�kler sanal"
else:
    X1=(-b+D**1/2)/(2*a)
    X2=(-b+D**1/1)/(2*a)
    print "X1",X1
    print "X2",X2
    
