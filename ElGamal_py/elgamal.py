'''

Implémentation du cryptosystème ElGamal

Devoir 1 - Preuve en cryptographie
Auteur : Chloé BENSOUSSAN

'''

import random
import math

# TODO : Implémenter un fonction retournant si mon cipher est un résidu quadratique ou pas (donc mon message aussi)

''' 
    Fonction de vérification que g est un générateur dans le groupe d'ordre q
    
    Fonction compute_generator :
    À partir d'un g, on calcul le générateur de q le plus proche 
'''


def is_generator(q, g):
    group = [i for i in range(1, q)]
    for i in range(1, q):
        try:
            n = g**i % q
            group.remove(n)
        except:
            return False
    return True


def compute_generator(q, g):
    gTmp = g
    while is_generator(q, gTmp) == False & gTmp < q:         # Chercher un générateur dans toutes les valeurs supérieurs ou égale à g
        gTmp = gTmp + 1

    if is_generator(q, gTmp):
        return gTmp
    else:
        gTmp = g - 1
        while not is_generator(q, gTmp) & gTmp > 0:         # Chercher un générateur dans toutes les valeurs inférieurs à g
            gTmp = gTmp - 1

        if is_generator(q, gTmp):
            return gTmp
        else:
            return -1


'''
    Fonction de vérification que n est premier
     
    Fonction générateur :
    Prend un nombre aléatoire et trouve le premier nombre premier supérieur ou égal à celui-ci
'''


def is_prime(n):                                # Cette fonction vérifie si n est premier
    if n == 2:
        return True

    if n % 2 == 0:                              # Vérification des nombres pair
        return False

    for i in range(3, int(math.sqrt(n)), 2):
        if n % i == 0:
            return False
    return True


def generator_prime():
    p = random.randint(100, 10 ** 4)

    if p % 2 == 0:                              # On le transforme en nombre impair
        p = p + 1

    while is_prime(p) == False:
        p = p + 2

    return p


''' 
    Fonction générateur de clés :
    Cette fonction génère les clés publiques et privée
'''


def generator_keys():
    prime1 = generator_prime()                  # Génération de deux nombres premiers
    prime2 = generator_prime()

    q = max(prime1, prime2)                     # q a la plus grande valeur
    g = min(prime1, prime2)

    q = 23
    print("Verification : Is", q, "prime ?", is_prime(q))

    g = compute_generator(q, g)                 # Calculer/Trouver un générateur à partir du deuxième nombre premier
    print("Vérification : Is <" + str(g) + "> a generator ?", is_generator(q, g))
    print("Is", g, "prime ?", is_prime(g))
    print("")

    if g == -1:
        print("Le programme n'a pas trouvé de générateur pour cet ordre de groupe. Relancer le programme.")
        exit()

    x = random.randint(1, q - 1)                # Clé secrète entre [1, q-1]
    h = g ** x % q                              # Clé publique

    return q, g, h, x


''' 
    Fonction d'encryptage
'''


def encryption(m, pk):
    y = random.randint(1, pk[0] - 1)            # Valeur aléatoire entre [1, q-1]
    c1 = pk[1] ** y % pk[0]                     # Première valeur du chiffré (indice sur le random y)
    s = pk[2] ** y % pk[0]

    c2 = m * s                                  # Deuxième valeur du chiffré (message m chiffré)
    return c1, c2


''' 
    Fonction de décryptage
'''


def decryption(cipher, pk, x):
    s = cipher[0] ** x % pk[0]                  # Calcul de c1^(-x) % q
    m = cipher[1] / s % pk[0]                   # Calcul de c2*c1^(-x)

    return m


''' 
    Fonction qui vérifie si n est un résidu quadratique par rapport à q
'''

def is_residu_quadratique(q, n):
    for i in range(1, q):
        if (i**2) == (n % q):
            return True
    return False


'''
    MAIN
'''


m = 6                                         # Message à crypter

ret = generator_keys()                          # Résultat du générateur
pk = (ret[0], ret[1], ret[2])                   # Tuple de clés publique
sk = ret[3]                                     # Tuple de clé privée

print("pk =", pk, "sk =", sk)
print("Message =", m, "\n")

if m > pk[0]:
    print("Le message est trop grand pour cette clé.")
    exit()

cipher = encryption(m, pk)                      # Récupération des chiffrés
print("Encryption =", cipher)

print("Le cipher est-il un résidu quadratique de", pk[0], "?", is_residu_quadratique(pk[0], cipher[1]))
print("Le message est-il un résidu quadratique de", pk[0], "?", is_residu_quadratique(pk[0], m))


decrypt = int(decryption(cipher, pk, sk))       # Message décrypté
print("Décryption =", decrypt)


print("\nIs decryption equal to the message ?", decrypt == m)
