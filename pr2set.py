X={23, 54, 74, 12, 32}
Y={45, 73, 12, 33, 157}
reuniune = X.union(Y)
print("a) X reuniune cu Y =", reuniune)
intersectie = X.intersection(Y)
print("b) X intersecte cu Y =",intersectie)
dif1 = X - Y
print("c) X - C =", dif1)
dif2 = Y - X
print("d) (X-Y) in reuniune cu (Y-X) =", dif1.union(dif2))
print("e) (X-Y) in intersectie cu (Y-X) =", dif2.intersection(dif1))