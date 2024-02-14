#A1

def A1():
    message=input("Saisi ton message :")
    n = len(message)
    i=0
    cpt=0
    while (i<n):
        if message[i]=="a":
            cpt+=1
        i+=1
    return cpt

def A2():
    message=input("Saisi ton message :")    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = "ABCDEFGHIIKLMNOPQRSTUVWXYZ"
    n = len(message)
    result=[0]*len(alphabet)
    for i in range(len(message)):
        if(message[i] in alphabet):
            result[alphabet.index(message[i])] +=1
        elif(message[i] in ALPHABET):
            result[ALPHABET.index(message[i])] +=1
    #result=[1, 1, 1, 0, 2, 0, 0, 0, 0, 1, 0, 2, 2, 2, 4, 0, 0, 1, 1, 1, 2, 1, 0, 0, 0, 1]
    indices_max=[i for i in range(len(result)) if(result[i]==max(result))]
    premiere_lettre=""
    petit_indice=len(alphabet)-1
    for i in range(len(indices_max)):
        if (indices_max[i]<petit_indice):
            petit_indice=alphabet.index(alphabet[indices_max[i]])
    return alphabet[petit_indice]



print(A2())
