"""
1)

Fonction suivant(un:type entier)

Début

    Si n==1 Alors
        Retourner(1)
    Sinon
        Si n%2==0
            Retourner(n/2)
        Sinon
            Retourner(n*3+1)
        Fin Si
    Fin Si
Fin Fonction

2) Cet algorithme effectue la fonction suivant (n) puis recommence avec le résultat obtenu jusqu'a obtenir 1. Toutes les valeurs obtenues par suivant(n) sont ensuite retournée avec un '-' entre chaque chiffres

3) 

Fonction trajet(n:type entier)

Début
    result = []

    TantQue suivant(n)!=1 Faire
        n=suivant(n)
        result.append(n)
    
    FinTantQue
    Retourner result
FinFonction
        
Fonction max(n):
    


"""