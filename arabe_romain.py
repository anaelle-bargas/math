romain=["M", "D", "C", "L", "X", "V", "I"]
arabe=[1000, 500, 100, 50, 10, 5, 1]

def arabe_romain(nb_a):
    nb_r=""
    i=0
    while nb_a>0:
        if(arabe[i]<=nb_a):
            nb_a-=arabe[i]
            nb_r+=romain[i]
        i+=1
    return nb_r



print(arabe_romain(611))