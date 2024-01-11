romain=["M", "D", "C", "L", "X", "V", "I"]
arabe=[1000, 500, 100, 50, 10, 5, 1]


# def romain_arabe(nb_r):
#     nb_a=0
#     # for i in range(0, len(nb_r)-1):
        
#     #     index=romain.index(nb_r[i])
#     #     index_chiffre_apres=romain.index(nb_r[i+1])
#     #     print(i, arabe[index_chiffre_apres], arabe[index], nb_a)


#     #     if(arabe[index_chiffre_apres]<=arabe[index]):
#     #         if(i==(len(nb_r)-2)):
#     #             nb_a+=arabe[index_chiffre_apres]
#     #         nb_a+=arabe[index]
#     #     else:
#     #         nb_a+=arabe[index_chiffre_apres]-arabe[index]
#     #         print("bla")
#     #         i+=2
#     i=0
#     while i<len(nb_r)-1:
#         index=romain.index(nb_r[i])
#         index_chiffre_apres=romain.index(nb_r[i+1])
#         print(i, arabe[index_chiffre_apres], arabe[index], nb_a)


#         if(arabe[index_chiffre_apres]<=arabe[index]):
#             if(i==(len(nb_r)-2)):
#                 nb_a+=arabe[index_chiffre_apres]
#             nb_a+=arabe[index]
#             i+=1

#         else:
#             nb_a+=arabe[index_chiffre_apres]-arabe[index]
#             print("bla")
#             i+=2
        
        
            

#     return nb_a


def romain_arabe(nb_r):
    if(len(nb_r)==1):
        return arabe[romain.index(nb_r[0])]
    elif(len(nb_r)<1):
        return 0

    else:
        chiffre0 = arabe[romain.index(nb_r[0])]
        chiffre1= arabe[romain.index(nb_r[1])]
        if(chiffre0>=chiffre1):
            return chiffre0 + romain_arabe(nb_r[1:])
        else:
            return chiffre1-chiffre0 + romain_arabe(nb_r[2:])



print(romain_arabe("DCLXXI"))

print(romain_arabe("XIV"))