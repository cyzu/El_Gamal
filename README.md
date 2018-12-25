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

### Déchiffrement

## Professeur

Madame **Tamara REZK** - Chercheur chez Inria

## Autheur

* Chloé Bensoussan - [cyzu](https://github.com/cyzu)
