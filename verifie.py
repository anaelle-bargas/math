#exo1
def verifie(l):
    for i in range(0, len(l)-1):
        if (l[i]>l[i+1]):
            return False
    return True

# print(verifie([0, 5, 8, 8, 9]))
# print( verifie([8, 12, 4]))
# print(verifie([-1, 4]))
# print( verifie([5]))

#exo2

def depouille(votes : list):
    res={}

    for i in range (0, len(votes)):
        if votes[i] not in res.keys():
            res[votes[i]]=1
        else:
            res[votes[i]]+=1

    return res

def vainqueur(res):
    contenu = res.items()
    max = [0]
    print(contenu)
    imax = [0]
    for i, j in res.items():
        if j > max[0]:
            max = [j]
            imax = [i]
        elif j == max[0]:
            max.append(j)
            imax.append(i)
    vainqueur={}
    for i in range(0, len(max)):
        vainqueur[imax[i]] =max[i]


    return vainqueur

       
print(vainqueur(depouille(['A', 'A', 'A', 'B', 'C', 'C', 'B', 'C'])))