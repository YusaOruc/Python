kontrol=True
i=1
while kontrol:
    a=int(raw_input("�ifreyi giriniz"))
    if a==123:
        print "Ho�geldiniz"
        kontrol=False
    elif i<3:
        print"tekrar deneyiniz"
        i=i+1
    else:
        print "bloke"
        kontrol=False
     
        
