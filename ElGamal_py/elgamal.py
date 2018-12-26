'''

Implémentation du cryptosystème ElGamal

Devoir 1 - Preuve en cryptographie
Auteur : Chloé BENSOUSSAN

'''

import random

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
         73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
         157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
         239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
         331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
         421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
         509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
         613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
         709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
         821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
         919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


''' 
    Fonction générateur :
    Cette fonction génère les clés publiques et privée
'''
def generator():
    q = random.choice(prime)
    g = random.choice(prime)

    while q < 100:
        q = random.choice(prime)        # Nombre premier supérieur à 100

    while g >= q:
        g = random.choice(prime)        # Un générateur de Zq (premier inférieur à q

    x = random.randint(1, q-1)          # Clé secrète entre [1, q-1]
    h = g ** x % q                      # Clé publique

    return q, g, h, x

''' 
    Fonction d'encryptage
'''
def encryption(m, pk):
    y = random.randint(1, pk[0]-1)      # Valeur aléatoire entre [1, q-1]
    c1 = pk[1] ** y % pk[0]             # Première valeur du chiffré (indice sur le random y)
    s = pk[2] ** y % pk[0]

    c2 = m * s                          # Deuxième valeur du chiffré (message m chiffré)
    return c1, c2

''' 
    Fonction de décryptage
'''
def decryption(cipher, pk, x):
    s = cipher[0] ** x % pk[0]          # Calcul de c1^(-x) % q
    m = cipher[1] / s                   # Calcul de c2*c1^(-x)

    return m


m = 56296                               # Message à crypter

ret = generator()                       # Résultat du générateur
pk = (ret[0], ret[1], ret[2])           # Tuple de clés publique
sk = ret[3]                             # Tuple de clé privée

cipher = encryption(m, pk)              # Récupération des chiffrés
decrypt = decryption(cipher, pk, sk)    # Message décrypté

print("pk =", pk, "sk =", sk)
print("Message =", m)
print("Encryption =", cipher)
print("Décryption =", decrypt)