persoane = [(18, 189, 67, "Masculin", "Necasatorit"),
(22, 177, 75 , "Masculin", "Casatorit"),
(25, 175, 68, "Feminin", "Necasatorita"),
(17, 160, 60, "Feminin", "Necasatorita"),
(19, 158, 62, "Feminin", "Casatorita"),
(27, 174, 71, "Feminin", "Necasatorita"),
(22, 180, 69, "Feminin", "Necasatorita")]
q=0
for i in range(0, len(persoane)):
    if persoane[i][0] < 20:
        q+=1
    else:
        q+=0
print("a) Procentul persoanelor sub 20 de ani: ", ((q)/len(persoane))*100)

a=0
for i in range(0,len(persoane)):
    if persoane[i][1] > 170:
        a+=1
    else:
        a+=0
print("b) Procentul persoanelor cu inaltimea mai mare de 170cm: ", ((a)/len(persoane))*100)

z=0
n1=0
for i in range(0,len(persoane)):
    if persoane[i][0] > 18:
        z+=1
        n1+=persoane[i][2]
print("b) Masa medie a unei persoane de peste 18 ani: ", (n1)/(z))

nrf = 0
nrfn = 0
for i in range(0, len(persoane)):
    if persoane[i][3]=="Feminin":
        nrf+=1
    else:
        nrf+=0
    if persoane[i][3]=="Feminin" and persoane[i][0]>20 and persoane[i][4]=="Necasatorita":
        nrfn+=1
    else:
        nrfn+=0
print("d) Procentul femeilor mai mari de 20 ani si necasatorite: ", (nrfn/nrf)*100)

cols = len(persoane[2])
masamedie = 0
for i in range(0, len(persoane)):
    masamedie += (sum(cols))/len(persoane)
print("Masa medie a tuturor persoanelor: ", masamedie)
y=0
for i in range(0, len(persoane)):
    if persoane[i][0]>20 and persoane[i][0]<50 and masamedie>persoane[i][2]:
        y+=1
    else:
        y+=0
print("e) Procentul peroanelor intre 20 si 50 de ani care au greutatea mai mare ca greutatea medie: ", ((y)/5)*100)
