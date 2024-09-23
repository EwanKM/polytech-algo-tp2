from math import sqrt


a = int(input("Entrez la valeur : "))

def premier(n):
    if n%2 == 0:
        return False
    for chiffre in range(2,n):
        if n%chiffre == 0:
            return False
    return True


print(premier(a))