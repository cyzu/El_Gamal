'''

Implémentation du cryptosystème ElGamal

Devoir 1 - Preuve en cryptographie
Auteur : Chloé BENSOUSSAN

'''

import random
import math


quadratic_residues =[]


''' 
    Fonctions utiles ------------------------------------------------------------------------------------------------
'''


def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)


def is_generator(q, g):
    group = [False for i in range(1, q)]  # Création d'un tableau de booléan
    for i in range(1, q):
        n = g**i % q

        if group[n-1] == True:              # Si la valeur est déjà obtenue, ce n'est pas un générateur
            return False
        else:
            group[n-1] = True
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


def generator_generator(q):
    group = [i for i in range(1, q)]    # Création du groupe

    for i in range(1, q):

        g = random.choice(group)                # Prendre un élément du groupe aléatoirement
        group.remove(g)

        if gcd(q, g) == 1 & is_generator(q, g):
            return g
    print("There is no generator for", q, "...")
    exit()


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

    prime = generator_prime()

    while not is_prime(2*prime + 1):                # Générer un nombre premier tel que 2*q+1 est aussi premier
        prime = generator_prime()

    q = (2 * prime) + 1

    #################################################################
    # q = 11
    #################################################################

    print("Verification : Is", q, "prime ?", is_prime(q))
    print("Verification : Is", prime, "prime ?", is_prime(prime))

    for i in range(0, q):
        if is_quadratic_residue(q, i):
            quadratic_residues.append(i)

    g = generator_generator(q)


    # g = 2
    print("Vérification : Is <" + str(g) + "> a generator ?", is_generator(q, g))
    print("")



    if g == -1:
        print("Le programme n'a pas trouvé de générateur pour cet ordre de groupe. Relancer le programme.")
        exit()

    x = random.randint(1, q - 1)  # Clé secrète entre [1, q-1]
    h = g ** x % q  # Clé publique

    return q, g, h, x


''' 
    Fonction Encryption / Décryption ---------------------------------------------------------------------------------
'''


def encryption(m, pk):
    m = quadratic_residues[m]
    print("Message après la bijection :", m)

    y = random.randint(1, pk[0] - 1)  # Valeur aléatoire entre [1, q-1]
    c1 = pk[1] ** y % pk[0]  # Première valeur du chiffré (indice sur le random y)
    s = pk[2] ** y % pk[0]

    c2 = m * s  # Deuxième valeur du chiffré (message m chiffré)
    return c1, c2


def decryption(cipher, pk, x):
    s = cipher[0] ** x % pk[0]  # Calcul de c1^(-x) % q
    m = cipher[1] / s % pk[0]  # Calcul de c2*c1^(-x)

    for i in range(0, len(quadratic_residues)):
        if quadratic_residues[i] == m:
            return i
    return False


''' 
    Fonction Calculant le résidue quadratique et le jacobi -----------------------------------------------------------
'''


def is_quadratic_residue(q, n):
    for i in range(1, q):
        if (i ** 2 % q) == (n % q):
            return True
    return False


# TODO big integer ! でかすぎてエラー
def compute_jacobi(q, n):
    r = n ** ((q - 1) / 2) % q
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

m = random.randint(1, len(quadratic_residues))  # Message à crypter

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
