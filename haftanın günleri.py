kontrol=True
while kontrol:
    x=int(raw_input("Say� de�erini giriniz"))
    if 1<=x<=365:
        a=x%7
        if a==0:
            print "Cumartesi"
        elif a==1:
            print "Pazar"
        elif a==2:
            print "Pazartesi"
        elif a==3:
            print "Sal�"
        elif a==4:
            print "�ar�amba"
        elif a==5:
            print "Per�embe"
        elif a==6:
            print "Cuma"
        kontrol=False
    else:
        print "Tekrar deneyiniz"
              
