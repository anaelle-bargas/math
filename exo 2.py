#exo1
def indices_maxi(lst):
    max = 0
    i = []
    for j in range(0, len(lst)):
        if max <= lst[j]:
            max = lst[j]
            
            if lst[j]==max:
                i.append(j)
            else:
                i=[j]
    return (max, i)


print(indices_maxi([21, 1, 21]))

#exo2
def positif(pile):
    pile_1 = list(pile)
    pile_2 = []
    while pile_1 != []:
        x = pile_1.pop()
        if x >= 0:
            pile_2.append(x)
    while pile_2 != []:
        x = pile_2.pop()
        pile_1.append(x)
    return pile_1
print(positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]))
print(positif([-2]))