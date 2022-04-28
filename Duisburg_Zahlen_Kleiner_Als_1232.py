z = 0
duisburg_zahl = 7
liste = []
qs = 0
while z < 1232:
    for i in str(z):
        qs += int(i)
    if qs == duisburg_zahl:
        liste.append(z)
        print(z)
    qs = 0
    z = int(z)
    z += 1
print("Es gibt",len(liste), "Duisburg-Zahl(en), die kleiner als 1232 ist/sind.")