# Cours de *Preuve en cryotographie*

Université de Nice Sophia-Antipolis
Master 2 IFI-CASPAR

## Premier travail

Le premier travail à rendre consiste à programmer El Gamal incluant une fonction de générateur, une fonction de chiffrement et une fonction de déchiffrement.

### Générateur

On définit un nombre premier ```P```, puis on on prend deux valeurs ```a``` et ```m``` tels que 
```
0 ≦ a ≦ P-2
0 ≦ m ≦ P-1
```

Puis on calcul ```n```  tel que ```n = m^a mod P```.

La clé publique est le triplet ```(P, m, n)```, et la clé secrète est ```a```.

### Chiffrement

Générer une valeur aléatoire  ```r```.
Calculer  ```c1 = m^r mod P``` et  ```c2 = message_a_crypter * n^y```.

Le chiffré est le tuple  ```(c1, c2)```. 

### Déchiffrement

Calculer  ```c2 / c1^a```.  Si tous les calculs sont corrects nous retrouvons le message initial.

## Deuxième travail

Nous allons introdiure la notion de résidue quadratique : ajouter une fonction déffissant si le message et le chiffré  ```c2```  sont des résidue quadratique.
```
pour i allant de 1 à q-1
si i^2 mod P est égale à x mod P, alors x est un résidu quadratique de P
```

Nous remarquons que lorsque le chiffré est un résidu quadratique, le message l'est aussi : il y a donc une fuite de 1 bit d'information dans cette encryption.

## Troisième travail

Nous allons donc sécurisé ElGamal pour ne pas avoir de fuite d'information.

- Utiliser les safe primes pour la valeur de ```P``` : ```P = q*2 + 1``` tels que ```P``` et  ```q``` sont des nombres premiers.
- ```m``` doit être un générateur de ```P``` et le ```gcd(P, m) == 1```.
- Restreindre le message dans l'ensemble des résidues quadratiques :
```
Créer la liste rq[] de résidus quadratique de P.
0 ≦ message ≦ len(rq)
message = rq[message]
```
- Après la décryption, retrouver le message en recherchant :
```
pour i allant de 0 à len(rq)
si rq[i] est égale à message_decrypter, retourner i
```

Il n'y a donc plus de fuite d'informations et ElGamel est maintenant sûr.

## Professeur

Madame **Tamara REZK** - Chercheur chez Inria 

## Autheur

* Chloé Bensoussan - [cyzu](https://github.com/cyzu)
