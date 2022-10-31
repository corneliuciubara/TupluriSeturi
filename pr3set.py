m = {1,3,6,7}
l = {4,7,8,3}
k = {5,8,4,1}
X = list(m)
Y = list(l)
Z = list(k)
print("Set 1 =",m)
print("Set 2 =",l)
print("Set 3 =",k)
for i in range(0,len(X)):
    for o in range(0,len(Y)):
        for p in range(0,len(Z)):
            if (-1)*(X[i]|Y[o]|Z[p]) == (-1)*(X[i])&(-1)*(Y[o])&(-1)*(Z[p]) and  (-1)*(X[i]&Y[o]&Z[p]) == (-1)*(X[i])|(-1)*(Y[o])|(-1)*(Z[p]):
                print("Se respecta prima lege al lui Morgan")