from math import *
def arabe_dec():

    lst1 = ["M", "D", "C", "L", "X", "V", "I"]
    lst2 = [1000, 500, 100, 50, 10, 5, 1]
    print("entrer un nombre romain :")
    nb_rom=input()
    l=len(nb_rom)
    nb_dec=0
    conforme= [i for i in nb_rom if i not in lst1]
    if conforme!=[]:
        return "la chaine entrée n'ets pas conforme"
    
    for i in range(1, l):
        if(lst1.index(nb_rom[i])>lst1.index(nb_rom[i-1]) or lst1.index(nb_rom[i])==lst1.index(nb_rom[i-1])):
            nb_dec+=lst2[lst1.index(nb_rom[i-1])]
                     

        else:
            nb_dec-=lst2[lst1.index(nb_rom[i-1])]

    return nb_dec+lst2[lst1.index(nb_rom[-1])]
print(arabe_dec())