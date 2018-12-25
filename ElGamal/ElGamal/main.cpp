//
//  main.cpp
//  El Gamal
//
//  Created by Chloé Yukino on 24/12/2018.
//  Copyright © 2018 Chloé Bensoussan. All rights reserved.
//

#include <iostream>
#include <stdlib.h>
#include <cmath>

#define P 661

void generator(int *pk, int &sk){
    pk[0] = P;             // Première valeur de la clé publique : un nombre premier
    sk = 7; // Choisir la clé secrète entre 0 et P-2 inclus
//    sk = rand() % (P - 1); // Choisir la clé secrète entre 0 et P-2 inclus
    pk[1] = 23.0;  // Choisir un nombre entre 0 et P-1 inclus
//    pk[1] = rand() % P;  // Choisir un nombre entre 0 et P-1 inclus
    
    double n = pow(pk[1], sk);
    printf("n = %lf\n", n);     // !!!!!!!!!!!!!!!! POW() RENVOI UN DOUBLE, PEUT PAS CASTER EN INT ÇA FAIT DES NOMBRES NÉGATIFS
    pk[2] = (int)n % P;
}

int main(int argc, const char * argv[]) {
    
    int pk[3], sk;
    srand(time(NULL));
    
    generator(pk, sk);
    
    printf("PK : (%d, %d, %d)       SK : %d\n", pk[0], pk[1], pk[2], sk);
//    printf("pow 7^3 = %lf\n", pow(pk[1], sk));
//    printf("345.0000 % 4 = %d\n", (int)345.0000%4);
    return 0;
}
