persoane = [
    (18, 189, 67, "Masculin", "Necasatorit"),
    (22, 177, 75, "Masculin", "Casatorit"),
    (25, 175, 68, "Feminin", "Necasatorita"),
    (17, 160, 60, "Feminin", "Necasatorita"),
    (19, 158, 62, "Feminin", "Casatorita"),
    (27, 174, 71, "Feminin", "Necasatorita"),
    (30, 174, 50, "Feminin", "Necasatorita"),
    (22, 180, 69, "Feminin", "Necasatorita")
]

nrPersoaneSub20 = 0
for i in range(0, len(persoane)):
    age,height,weight,sex,married = persoane[i]
    if age < 20:
        nrPersoaneSub20+=1

print("a) Procentul persoanelor sub 20 de ani: ", ((nrPersoaneSub20)/len(persoane))*100)

nrPersoane170plus = 0
for i in range(0,len(persoane)):
    age,height,weight,sex,married = persoane[i]
    if height > 170:
        nrPersoane170plus+=1

print("b) Procentul persoanelor cu inaltimea mai mare de 170cm: ", ((nrPersoane170plus)/len(persoane))*100)

nrPersoaneMasaMedie18plus = 0
mamaTotala18plis = 0
for i in range(0,len(persoane)):
    age,height,weight,sex,married = persoane[i]
    if age > 18:
        nrPersoaneMasaMedie18plus+=1
        mamaTotala18plis+=weight
if (nrPersoaneMasaMedie18plus>0):
    print("b) Masa medie a unei persoane de peste 18 ani: ", (mamaTotala18plis)/(nrPersoaneMasaMedie18plus))
else:
    print("e) date insuficiente")

nrf = 0
nrfn = 0
for i in range(0, len(persoane)):
    age,height,weight,sex,married = persoane[i]
    if sex=="Feminin":
        nrf+=1
    if sex=="Feminin" and age>20 and married=="Necasatorita":
        nrfn+=1
if (nrf>0):
    print("d) Procentul femeilor mai mari de 20 ani si necasatorite: ", (nrfn/nrf)*100)
else:
    print("e) date insuficiente")

# Calculam masa medie
masaTotala=0
for i in range(0,len(persoane)):
    age,height,weight,sex,married = persoane[i]
    masaTotala += weight
masaMedie = masaTotala / len(persoane)
print("Masa medie a tuturor persoanelor: ", masaMedie)

cnt2050=0
cnt2050masa=0
for i in range(0,len(persoane)):
    age,height,weight,sex,married = persoane[i]
    if age>20 and age<50:
        cnt2050+=1
    if age>20 and age<50 and masaMedie<weight:
        cnt2050masa+=1
if (cnt2050>0):
    print("e) Procentul peroanelor intre 20 si 50 de ani care au greutatea mai mare ca greutatea medie: ",
      (cnt2050masa/cnt2050)*100)
else:
    print("e) date insuficiente")
