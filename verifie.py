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


       
print(depouille(['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']))