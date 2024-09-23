"""
Exercice 1  
"""
#a = int(input("Entrez la valeur : "))

def premier(n):
    if n%2 == 0:
        return False
    for chiffre in range(2,n):
        if n%chiffre == 0:
            return False
    return True


#print(premier(a))
"""
Exercice 2
"""
n2 = 5
nb_premiers = 0
variable = 2
liste = [2]
while nb_premiers < n2-1 :
    if premier(variable) == True :
        liste.append(variable)
        nb_premiers += 1
    variable +=1
print(liste)