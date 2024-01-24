#exo1

def moyenne(liste):
    somme=0
    coeffs=0
    for i in range(0, len(liste)):
        somme+=liste[i][0]*liste[i][1]
        coeffs+=liste[i][1]
    if coeffs==0:
        return None
    else:
        
        return somme/coeffs

print(moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))

print(moyenne([(3, 0), (5, 0)]))

#exo2


coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
 
def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par
    des " *" , les 0 par deux espaces " ".
    La valeur "" donnée au paramètre end permet de ne pas avoir
    de saut de ligne.'''
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(" *", end= "")
            else:
                print(" ", end= "")
        print()
    
    
def zoomListe(liste_depart, k):
    '''renvoie une liste contenant k fois chaque
    élément de liste_depart'''
    liste_zoom = []
    for elt in liste_depart :
        for i in range(k):
            liste_zoom.append(elt)
    return liste_zoom
    
def zoomDessin(grille, k):
    '''renvoie une grille où les lignes sont zoomées k fois
    ET répétées k fois'''
    grille_zoom = []
    for elt in grille:
        liste_zoom = zoomListe(elt, k)
        for i in range(k):
            grille_zoom.append(liste_zoom)
    return grille_zoom
    
print(affiche(coeur))
print(affiche(zoomDessin(coeur, 3)))
    