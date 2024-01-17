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
    res={"A":2, "B":8}
    print(res.keys())
    for i in range (0, len(votes)):
        print(votes[i] in res.keys())
        
        print(votes[i])
       
depouille(['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B'])