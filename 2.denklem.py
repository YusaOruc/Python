a=int(raw_input("bir say� girin:"))
b=int(raw_input("bir say� girin:"))
o=b**2-4*a*c
if o>0:
    x1=(-b+o**1/2)/2*a
    x2=(-b-o**1/2)/2*a
    print "x1",x1,"x2",x2
elif o==0:
    x=(-b/2*a)
    print "x",x
else:
       print "real k�k yoktur"
