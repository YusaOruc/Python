sicilno=int(raw_input("sicilnoyu girin"))
calsa=int(raw_input("�al��ma saatini girin"))
sauc=int(raw_input("saatlik �al��ma saatini girin"))
maas=calsa*sauc
prim=maas*0.14
vergi=maas*0.15
netmaas=maas-(vergi+prim)
print sicilno,"sicilno"
print netmaas,"netmaas"
print prim,"vergi"
print vergi,"vergi"
