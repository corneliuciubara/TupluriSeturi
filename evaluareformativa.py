p = [(4, "Lapte", 31.10, 2.11, 25), 
(7, "Castraveti", 22.10, 10.11, 46),
(8, "Iaurt", 11.10, 10.11, 22),
(4, "Mere", 25.10, 1.11, 34), 
(7, "Cascaval", 22.10, 1.11, 46),
(8, "Carne de vita", 11.10, 1.11, 22),
(4, "Tomate", 25.10, 1.11, 33)]
datacurenta = 2.11
print("a) Produsele expirate:")
for i in range(0, len(p)):
    if p[i][3] <= datacurenta:
        print(p[i][1])
    
print("b) Produsele cu reducere de 50%:")
for i in range(0, len(p)):
    if p[i][3]*0.25 == datacurenta:
        print(p[i][1])

print("c) Produsele cu reducere de 20%:")
for i in range(0, len(p)):
    if datacurenta == (p[i][2]+p[i][3]/2):
        print(p[i][1])
  

print("d) Produsele cu termen de valabilitate de cel putin 1 an:")
for i in range(0, len(p)):
    if p[i][2]+p[i][3]>365:
        print(p[i][1])
    
print("e) Lista produselor cu termen de valabilitate de cel mult o luna:")
for i in range(0, len(p)):
    if p[i][2]+p[i][2]>30:
        print(p[i][1])
print("Nu sunt produse cu termen de valabilitate de cel mult o luna")



