# 1.

def note_option():
    note_option=int(input("note_option"))
    points_gagnes=0
    if note_option<10:
        points_gagnes=0
    else:
        points_gagnes=note_option-10
    points_gagnes=points_gagnes*2
    return points_gagnes

def stock_notes():
    matieres=["Français", "Mathématiques", "H-G", "LV1", "LV2", "Phy", "Techno"]
    notes=[]
    for i in range(7):
        notes.append(int(input("Entrez la note"+matieres[i])))
    return notes

def total_points():
    coeff=[3, 3, 2, 2, 1, 2, 1]
    notes=stock_notes()
    points=0
    for i in range(7):
        points+=notes[i]*coeff[i]

    points+=note_option()
    return points

def recu():
    points = total_points()
    coeff=[3, 3, 2, 2, 1, 2, 1]
    add_coeff=0
    for i in range(7):
        add_coeff+=coeff[i]
    moy = points/add_coeff
    print(moy)
    if 10<=moy and moy <12:
        return "Reçu mention Passable"
    elif 12<=moy and moy<14:
        return "Reçu mention Assez Bien"
    elif 14<=moy and moy<16:
        return "Bien"
    elif moy>=16:
        return "Reçu mention Très Bien"
    else:
        return "Non reçu"

print(recu())
