# Lacatus Catalin-Petru, grupa 2341
#Algoritmi genetici

import math
import random

def calculeazaLungimeaCromozomului(stInterval, drInterval, precizie):
    return int(math.log(((drInterval - stInterval) * 10 ** precizie), 2) + 1)


def initPopulatie(matrice):
    for linie in matrice:
        for coloana in range(len(linie)):
            linie[coloana] =  str(random.choice([0,1]))
            # linie[coloana] = str(random.randint(0, 1))
    return matrice


def calculeazaValCorespCromozomuluiInDomeniulDeDef(s, stInterval, drInterval, lungimeCromozom, precizie):
    # print(s + "Asta e str")
    x = int(s, 2)
    # print(x)
    rez = (x * (drInterval - stInterval)) / (2 ** lungimeCromozom - 1) + stInterval
    # print(rez)
    return round(rez, precizie)

def calculeazaFunctie(valoare, parametri_functie_maximizat):
    return ((valoare ** 2) * parametri_functie_maximizat[0] + (valoare * parametri_functie_maximizat[1]) + parametri_functie_maximizat[2])

def populatieInitiala(g, matrice, stInterval, drInterval, lungimeCromozom, precizie, parametri_functie_maximizat, iteratie):
    suma = 0
    listaValoriF = []
    listaValoriX = []
    listaSume = []
    maxF = 0
    if iteratie == 1:
       g.write("Populatia initiala\n")

    for element in matrice:
        if iteratie == 1:
          g.write(str(matrice.index(element) + 1) + " : ")
        val = ""
        for j in range(0, len(element)):
            val = val + element[j]

        x = calculeazaValCorespCromozomuluiInDomeniulDeDef(val, stInterval, drInterval, lungimeCromozom, precizie)
        listaValoriX.append(x)

        f = calculeazaFunctie(x, parametri_functie_maximizat)

        if f > maxF:
            maxF = f
        listaValoriF.append(f)
        suma = suma + f
        listaSume.append(suma)

        if iteratie == 1:
            g.write(val + " x= " + str(x) + " f= " + str(f) + '\n')
    if iteratie==1:
       g.write("------------------------------------------------------------------------\n")
    return suma,listaValoriX, listaValoriF, listaSume, maxF

def calcProbabSelectie(sumaF, listaValoriF,iteratie):
    listaProbab = []
    if iteratie==1:
        g.write("Probabilitati selectie\n")
    for elem in listaValoriF:
        probab = elem / sumaF
        listaProbab.append(probab)
        if iteratie==1:
          g.write("cromozom   " + str(listaValoriF.index(elem) + 1) + " probabilitate " + str(probab) + '\n')
    if iteratie==1:
        g.write("------------------------------------------------------------------------\n")
    return listaProbab


def cautareBinara(listaProbabSelectie, st, dr, el):
    raspuns = -1
    while st<=dr:
        m = (st + dr) // 2
        if listaProbabSelectie[m] > el:
            raspuns = m
            dr = m-1
        else:
            st = st + 1
    return raspuns

def selectie(listaProbabSelectie, dimensiunePopulatie,iteratie):
    listaCromozomiRecombinare = []
    for i in range(dimensiunePopulatie):
        u = random.random()
        cromozomIndice = cautareBinara(listaProbabSelectie, 0, dimensiunePopulatie -1, u)
        if iteratie==1:
            g.write("\nu= " + str(u) + " selectam cromozomul " + str(cromozomIndice+1))
        cromozom = "".join(matrice[cromozomIndice])
        listaCromozomiRecombinare.append(cromozom)
    return listaCromozomiRecombinare

def PopulatieNoua(g, listaCromozomiNoua, stInterval, drInterval, lungimeCromozom, precizie,parametri_functie_maximizat): #
    cromozomI = 1
    for element in listaCromozomiNoua:
        cromozom = "".join(element)
        x = calculeazaValCorespCromozomuluiInDomeniulDeDef(cromozom, stInterval, drInterval, lungimeCromozom, precizie)
        f = calculeazaFunctie(x,parametri_functie_maximizat)
        g.write(str(cromozomI)  +" : "+ cromozom + " " + "x= " + str(x) + " f= " + str(f) + '\n')
        cromozomI+=1

def probabilitateDeIncrucisare(g, listaCromozomiRecombinare, probabilitateDeRecombinare, iteratie):
    listaCromozomiCareParticipa = []
    if iteratie==1:
        g.write("Probabilitatea de recombinare/incrucisare\n")
    for i in range(len(listaCromozomiRecombinare)):
        u = random.random()
        if u<probabilitateDeRecombinare:
            if iteratie==1:
                g.write(str(i+1) + " " + listaCromozomiRecombinare[i] + " u= " + str(u) + " < " + str(probabilitateDeRecombinare) + " participa \n")
            listaCromozomiCareParticipa.append(i)
        else :
            if iteratie==1:
                g.write(str(i+1) + " " + listaCromozomiRecombinare[i] + " u= " + str(u) + "\n")
    if iteratie == 1:
        g.write("\n------------------------------------------------------------------------\n")
    return listaCromozomiCareParticipa

def recombinareCromozomi(g, listaCromozomiRecombinare, listaCromozomiCareParticipa, lungimeCromozom, iteratie):
    if iteratie==1:
        g.write("Recombinari \n")
    while len(listaCromozomiCareParticipa) > 1:
        p1 = random.choice(listaCromozomiCareParticipa)
        listaCromozomiCareParticipa.remove(p1)
        p2 = random.choice(listaCromozomiCareParticipa)
        listaCromozomiCareParticipa.remove(p2)
        punctRupere = random.randint(0, lungimeCromozom)
        copie = listaCromozomiRecombinare[p1]
        listaCromozomiRecombinare[p1] = listaCromozomiRecombinare[p1][0:punctRupere] + listaCromozomiRecombinare[p2][punctRupere:]
        listaCromozomiRecombinare[p2] = listaCromozomiRecombinare[p2][0:punctRupere] + copie[punctRupere:]
        if iteratie ==1:
            g.write("Recombinare dintre cromozomul " + str(p1+1) + " cu cromozomul " + str(p2+1) + " : \n")
            g.write(listaCromozomiRecombinare[p1] + " " + listaCromozomiRecombinare[p2] + " punct de rupere " + str(
                punctRupere) + "\n")
            g.write("Rezultat " + " " + listaCromozomiRecombinare[p1] + " " + listaCromozomiRecombinare[p2] + '\n')
    if iteratie==1:
        g.write("\n------------------------------------------------------------------------\n")

def mutatie(g, listaCromozomiRecombinare, probabilitateDeMutatie):
    listaMutatii = []
    for i in range(len(listaCromozomiRecombinare)):
        valoare = []
        valoare.extend(listaCromozomiRecombinare[i])
        for j in range(i):
            u = random.random()
            if u < probabilitateDeMutatie:
                if listaCromozomiRecombinare[i][j] == '1':
                    valoare[j] = '0'
                    listaMutatii.append(i)
                else:
                    valoare[j] = '1'
        listaCromozomiRecombinare[i] = "".join(valoare)
    return listaMutatii

def calculeazaEvolutie(g, listaCromozomiRecombinare, stInterval, drInterval, lungimeCromozom, precizie, parametri_functie_maximizat, dimensiunePopulatie):
    maxF = 0
    for element in listaCromozomiRecombinare:
        cromozom = "".join(element)
        x = calculeazaValCorespCromozomuluiInDomeniulDeDef(cromozom, stInterval, drInterval, lungimeCromozom,precizie)
        f = calculeazaFunctie(x, parametri_functie_maximizat)
        if f>maxF:
            maxF = f
    g.write("Valoarea maxima: ")
    g.write(str(maxF) + '\n')
    g.write("Valoarea medie a performantei: ")
    g.write(str(maxF/dimensiunePopulatie))
    g.write("\n------------------------------------------------------------------------\n")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------Citire date initiale------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
f = open("date.in", "r")
g = open("date.out", "w")

dimensiunePopulatie = int(f.readline())
# print(dimensiunePopulatie)

domeniuDeDefinitieAlFunctiei = f.readline().split()  # initializez pun valorile intr-o lista
stInterval = int(domeniuDeDefinitieAlFunctiei[0])  # initializez capatul st al intervalului
drInterval = int(domeniuDeDefinitieAlFunctiei[1])  # initializez capatul drept al intervalului
# print(stInterval, " ", drInterval)

parametri_functie_maximizat = tuple(map(int, f.readline().split()))  # creez un tuplu si fac fiecare valoare sa fie int
# print(parametri_functie_maximizat)

precizie = int(f.readline())
# print(precizie)

probabilitateDeRecombinare = float(f.readline())
# print(probabilitateDeRecombinare)

probabilitateDeMutatie = float(f.readline())
# print(probabilitateDeMutatie)

nrEtapeAlgoritm = int(f.readline())
# print(nrEtapeAlgoritm)

lungimeCromozom = calculeazaLungimeaCromozomului(stInterval, drInterval, precizie)
# print(lungimeCromozom)

matriceCrozomi = [["0" for i in range(lungimeCromozom)] for j in range(dimensiunePopulatie)]

matrice = initPopulatie(matriceCrozomi)

# for i in range(dimensiunePopulatie):
#     for j in range(dimensiunePopulatie):
#         print(matrice[i][j], end = ' ' )
#     print()

print("Datele dvs sunt in fisierul 'date.out'!")
for i in range(1, nrEtapeAlgoritm+1):
    sumaF, listaValoriX, listaValoriF, listaSume, maxF = populatieInitiala(g, matrice, stInterval, drInterval, lungimeCromozom, precizie,
                                                             parametri_functie_maximizat, i)

    listaProbabSelectie = calcProbabSelectie(sumaF, listaValoriF,i)

    listaSume2 = []
    afiseaza = str(0) + " "
    for el in listaSume:
        afiseaza = afiseaza + str(el / sumaF) + " "
        listaSume2.append(el / sumaF)
    if i==1:
        g.write("Intervale probabilitati selectie\n")
        g.write(afiseaza)
        g.write("\n------------------------------------------------------------------------\n")
    if i==1:
        g.write("Procesul de selectie \n")
        cromozom = "".join(matrice[listaValoriF.index(maxF)])
        g.write("Element etilitist " + str(matrice.index(matrice[listaValoriF.index(maxF)])+1)+ " : " + cromozom + " x= " + str(listaValoriX[listaValoriF.index(maxF)]) + "  f= " + str(maxF) + " -> trece in urmatoarea generatie")

    listaCromozomiRecombinare = selectie(listaSume2, dimensiunePopulatie,i)

    if i ==1:
        g.write("\n------------------------------------------------------------------------\n")
        g.write(" Dupa selectie \n")
        PopulatieNoua(g, listaCromozomiRecombinare, stInterval, drInterval, lungimeCromozom, precizie, parametri_functie_maximizat)
        g.write("\n------------------------------------------------------------------------\n")

    listaCromozomiCareParticipa = probabilitateDeIncrucisare(g, listaCromozomiRecombinare, probabilitateDeRecombinare,i)

    recombinareCromozomi(g, listaCromozomiRecombinare, listaCromozomiCareParticipa, lungimeCromozom,i)

    if i == 1:
        g.write("Dupa recombinare\n")
        PopulatieNoua(g, listaCromozomiRecombinare, stInterval, drInterval, lungimeCromozom, precizie, parametri_functie_maximizat)
        g.write("\n------------------------------------------------------------------------\n")

    listaMutatii = mutatie(g, listaCromozomiRecombinare, probabilitateDeMutatie)

    if i ==1:
        g.write("Probabilitate de mutatie pentru fiecare gena " + str(probabilitateDeMutatie) + '\n')
        g.write("Au fost modificati cromozomii: \n")
        for el in listaMutatii :
            g.write(str(el+1) + '\n')
        g.write("Dupa mutatie: \n")
        PopulatieNoua(g, listaCromozomiRecombinare, stInterval, drInterval, lungimeCromozom, precizie, parametri_functie_maximizat)
        g.write("\n------------------------------------------------------------------------\n")
    if i==1:
        g.write("Evolutia maximului \n")
    calculeazaEvolutie(g, listaCromozomiRecombinare, stInterval, drInterval, lungimeCromozom, precizie, parametri_functie_maximizat, dimensiunePopulatie)

