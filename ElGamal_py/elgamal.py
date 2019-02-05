'''

Implémentation du cryptosystème ElGamal

Devoir 1 - Preuve en cryptographie
Auteur : Chloé BENSOUSSAN

'''

import random
import math


quadratic_residues = []


''' 
    Fonctions utiles ------------------------------------------------------------------------------------------------
'''


# def is_generator(p, g):
#     group = [False for i in range(1, p)]  # Création d'un tableau de booléan
#     for i in range(1, p):
#         n = g**i % p
#
#         if group[n-1] == True:              # Si la valeur est déjà obtenue, ce n'est pas un générateur
#             return False
#         else:
#             group[n-1] = True
#     return True

def is_generator(group, p, g):
    test = [0 for i in range(1, max(group)+2)]
    for i in range(1, len(group)+1):
        n = g**i % p
        test[n] += 1
    for i in group:
        if test[i] != 1:
            return False
    return True




def is_prime(n):  # Cette fonction vérifie si n est premier
    if n == 2:
        return True

    if n % 2 == 0:  # Vérification des nombres pair
        return False

    for i in range(3, int(math.sqrt(n)), 2):
        if n % i == 0:
            return False
    return True


''' 
    Fonction générateur du nombre premier et d'un générateur --------------------------------------------------------
'''


# def generator_generator(p):
#     group = [i for i in range(1, p)]    # Création du groupe
#
#     for i in range(1, p):
#
#         g = random.choice(group)                # Prendre un élément du groupe aléatoirement
#         group.remove(g)
#
#         if math.gcd(p, g) == 1 & is_generator(p, g):
#             return g
#     print("There is no generator for", p, "...")
#     exit()

def generator_generator(p, q):
    g = random.randint(2, q)
    return g**2 % p


def generator_prime():
    p = random.randint(17, 2 ** 10)

    if p % 2 == 0:  # On le transforme en nombre impair
        p = p + 1

    while is_prime(p) == False:
        p = p + 2


    return p


''' 
    Fonction Générateur de clés -------------------------------------------------------------------------------------
'''


def generator_keys():

    q = generator_prime()

    while not is_prime(2*q + 1):                # Générer un nombre premier tel pue 2*q+1 est aussi premier
        q = generator_prime()

    p = (2 * q) + 1

    #######################
    p = 11
    q = 5
    #######################

    print("Verification : Is", p, "prime ?", is_prime(p))
    print("Verification : Is", q, "prime ?", is_prime(q))

    for i in range(0, p):
        if is_quadratic_residue(p, i):
            quadratic_residues.append(i)

    g = generator_generator(p, q)

    print("Vérification : Is <" + str(g) + "> a generator ?", is_generator(quadratic_residues, p, g))
    print("Vérification : Is <" + str(g) + "> a quadratic ?", is_quadratic_residue(p, g))
    print("")

    if g == -1:
        print("Le programme n'a pas trouvé de générateur pour cet ordre de groupe. Relancer le programme.")
        exit()

    x = random.randint(1, p - 1)  # Clé secrète entre [1, p-1]
    h = g ** x % p  # Clé publique

    return p, g, h, x


''' 
    Fonction Encryption / Décryption ---------------------------------------------------------------------------------
'''


def encryption(m, pk):
    m = quadratic_residues[m]
    # m = m**2 % pk[0]
    print("Message après la bijection :", m)

    y = random.randint(1, pk[0] - 1)  # Valeur aléatoire entre [1, p-1]
    c1 = pk[1] ** y % pk[0]  # Première valeur du chiffré (indice sur le random y)
    s = pk[2] ** y % pk[0]

    c2 = m * s  # Deuxième valeur du chiffré (message m chiffré)
    return c1, c2


def decryption(cipher, pk, x):
    s = cipher[0] ** x % pk[0]  # Calcul de c1^(-x) % p
    m = cipher[1] / s % pk[0]  # Calcul de c2*c1^(-x)

    for i in range(0, len(quadratic_residues)):
        if quadratic_residues[i] == m:
            return i

    # return square_root_mod(pk[0], m)
    return False


# Tonelli–Shanks algorithm
def square_root_mod(p, m):

    # Etape 1
    order = p-1
    puissance = 0
    while order % 2 == 0:
        order = order/2
        puissance += 1

    if order % 2 != 0:
        facteurOdd = order
    else:
        print("Algorithme de la racine carré modulaire échoué.")
        exit()

    # Etape 2
    nonResidue = random.randint(2, p-1)
    while is_quadratic_residue(p, nonResidue):
        nonResidue = random.randint(2, p - 1)

    # Etape 3
    c = nonResidue ** facteurOdd % p
    t = m ** facteurOdd % p
    r = m ** ((facteurOdd+1)/2) % p

    # Etape 4
    while t != 1 or t != 0:
        i = 1

        # trouver i tel que t^(2*i) % p = 1
        while (t ** 2 ** i) % p != 1:
            i = i + 1

        # b = c ** 2 ** (puissance-i-1)
        b = c ** 2 ** (puissance - i - 1) % p
        puissance = i
        c = b ** 2 % p
        t = t * (b ** 2) % p
        r = r * b % p

    if t == 0:
        return 0  # False
    if t == 1:
        return r




''' 
    Fonction Calculant le résidue quadratique et le jacobi -----------------------------------------------------------
'''


def is_quadratic_residue(p, n):
    for i in range(1, p):
        if (i ** 2 % p) == (n % p):
            return True
    return False


def compute_jacobi(p, n):
    r = n ** ((p - 1) / 2) % p
    if int(r) == 1:
        return 1
    else:
        return -1


'''
    MAIN -------------------------------------------------------------------------------------------------------------
'''

ret = generator_keys()  # Résultat du générateur de clés
pk = (ret[0], ret[1], ret[2])  # Tuple de clés publique
sk = ret[3]  # Tuple de clé privée

m = random.randint(2, len(quadratic_residues)-1)  # Message à crypter

print("pk =", pk, "sk =", sk)
print("Message =", m, "\n")

if m >= pk[0]:
    print("Le message est trop grand pour cette clé.")
    exit()

cipher = encryption(m, pk)  # Récupération des chiffrés
print("Encryption =", cipher)

# print("Le cipher est-il un résidu quadratique de", pk[0], "?", is_quadratic_residue(pk[0], cipher[1]))
# print("Le message est-il un résidu quadratique de", pk[0], "?", is_quadratic_residue(pk[0], m))
# print("")

decrypt = int(decryption(cipher, pk, sk))  # Message décrypté
print("Décryption =", decrypt)

print("\nIs decryption equal to the message ?", decrypt == m)
