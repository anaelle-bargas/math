#exo1
def a_doublon(lst):
    lst_2=[]
    for i in lst:
        if i in lst_2:
            return True
        else:
            lst_2.append(i)
    return False
print(a_doublon([]))
print(a_doublon([1]))
print(a_doublon([1, 2, 4, 6, 6]))
print(a_doublon([2, 5, 7, 7, 7, 9]))
print(a_doublon([0, 2, 3]))

#exo2