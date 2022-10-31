elevi = [("Ciubara", "Corneliu", "Masculin", 3, 9, 5), ("Betisor", "Vadim", "Masculin", 4, 10, 8),("Ion", "Cebotaros", "Masculin", 7, 1, 5),("Cornelia", "Dovgan", "Feminin", 9, 8, 2),("Vladimir", "Iatemirschi", "Masculin", 10, 10, 10)]

for i in range(0, len(elevi)):
    print("Nota medie a elevui",elevi[i][0:2] ,"este: ", sum(elevi[i][3:])/3)

for i in range(0, len(elevi)):
    if sum(elevi[i][3:])/3 < 5:
        print(elevi[i][0:2], "Elevii sunt restantieri")

for i in range(0, len(elevi)):
    if (sum(elevi[i][3:])/3 >= 9) and (elevi[i][3] >=9) and (elevi[i][4] >=9) and (elevi[i][5] >=9):
        print(elevi[i][0:2], "este eminent")

