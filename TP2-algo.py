"""
Exercice 1  
"""
a = int(input("Entrez la valeur : "))

def premier(n):
    if n%2 == 0:
        return False
    for chiffre in range(2,n):
        if n%chiffre == 0:
            return False
    return True


print(premier(a))
"""
Exercice 2
"""
variable = 2
def exo2(variable):
    n2 = int(input("Entrez le nombre que vous souhaitez : "))
    nb_premiers = 0
    liste = [variable]
    while nb_premiers < n2-1 :
        if premier(variable) == True :
            liste.append(variable)
            nb_premiers += 1
        variable +=1
    print(liste)
exo2(variable)
"""
Exercice 3
"""
def exo3():
    while True:
        try:
            borne_1 = int(input("borne 1 : "))
            borne_2 = int(input("borne 2 : "))
            
            # Vérification si borne_1 est plus grande que borne_2
            if borne_1 > borne_2:
                print("Erreur : La première borne doit être inférieure ou égale à la deuxième. Veuillez réessayer.")
            else:
                break  # Si tout est correct, on sort de la boucle
        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides. Réessayez.")
    list3 = []
    for loop in range(borne_1,borne_2):
        if premier(loop) == True:
            list3.append(loop)
    print(list3)
exo3()

"""
Exercice 4 
"""

while True : 
    try : 
        choix = int(input("Vous préférez une borne (1) ou deux (2) ? : "))
        if choix == 2 :
            exo3()
            break
        elif choix == 1 :
            borne_min = int(input("Entrez la borne minimale : "))
            exo2(borne_min)
            break
        else : 
            print("Erreur")
    except ValueError:
        print('Erreur :(')





