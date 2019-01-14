
def is_quadratic_residue(q, n):
    for i in range(1, q):
        if (i**2 % q) == (n % q):
            return 1
    return -1

def compute_jacobi(q, n):
    r = n**((q-1)/2)
    if int(r % q) == 1:
        return 1
    else:
        return -1

a = 11
for b in range(1, a):
    print(a, b, "->", is_quadratic_residue(a, b))

print("")
for b in range(1, a):
    print(a, b, "->", compute_jacobi(a, b))

a = 653
b = 453
print(a, b, '->', is_quadratic_residue(a, b))

b = 640
print(a, b, '->', is_quadratic_residue(a, b))

