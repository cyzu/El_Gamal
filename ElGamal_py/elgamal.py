'''

Implémentation du cryptosystème ElGamal

Devoir 1 - Preuve en cryptographie
Auteur : Chloé BENSOUSSAN

'''

import random

P = 17                              # Entier premier
M = 7                     # Message a crypter

# Fonction générateur
def generator():
    a = random.randint(0, P-2)      # Choisit un entier entre 0 et P-2 inclus
    g = random.randint(1, P-1)      # Choisit un entier entre 0 et P-1 inclus
    A = g**a % P                    # Clé secrète A = g^a % P

    return g, A, a

# Fonction de chiffrement
def chiffrement(p):
    k = random.randint(0, p[0])     # Choisir un entier en 0 et P, valeur choisit par la personne qui chiffre
    K = p[1]**k % p[0]              # Première valeur envoyé avec le message chiffré
    c = M*(p[2]**k) % p[0]          # Message M chiffré
    print("k aléa =", k)
    return K, c

# Fonction de déchiffrement
def dechiffrement(p, c, a):
    x = c[0] ** a % p[0]
    return (c[1]/x) % p[0]


result = generator()                # Récupération du tuple de generator()
pk = (P, result[0], result[1])      # Clé publique (P, g, A)
sk = result[2]                      # Clé privée (a)

chiffre = chiffrement(pk)           # Récupération du tuple envoyé (le chiffré)

print("pk =",pk , "sk =", sk)
print("Chiffré =", chiffre)

dechiffre = dechiffrement(pk, chiffre, sk)
print("Message déchiffré =",dechiffre)

