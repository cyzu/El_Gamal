
def is_residu_quadratique(q, n):
    for i in range(1, q):
        if (i**2) == (n % q):
            return True
    return False

a = 15
b = 2
print(a, b, "->", is_residu_quadratique(a, b))