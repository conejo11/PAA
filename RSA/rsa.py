import math
import random

def extendedEuclidean(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		gcd, x, y = extendedEuclidean(b % a, a)
		return (gcd, y - (b/a) * x, x)

def fermat(n):
    if n > 1:
        for t in range(5):
            rand = random.randint(2, n)-1
            if pow(rand,n-1,n) != 1:
                return False
        return True
    else:
        return False
