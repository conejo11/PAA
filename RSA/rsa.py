import math
import random

def extendedEuclidean(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		gcd, x, y = extendedEuclidean(b % a, a)
		return (int(gcd), int(y - (b/a) * x), int(x))

def fermatPrimalityTest(n):
    if n > 1:
        for t in range(50):
            rand = random.randint(2, n)-1
            if pow(rand,n-1,n) != 1:
                return False
        return True
    else:
        return False

def geraPrimo(bits):
    n = random.randint(0, pow(2, bits))
    if n % 2 == 0:
        n = n+1

    while not fermatPrimalityTest(n):
        print(n)
        n += 2

    return n

def chavePublica(bits):
    p = geraPrimo(bits)
    q = geraPrimo(bits)

    e = geraPrimo(8)
    while math.gcd(e, (p-1)*(q-1)) != 1:
        e = geraPrimo(16)

    return (e, p, q)

def chavePrivada(e, p, q):
    d = extendedEuclidean(e, (p-1)*(q-1))[1]
    #if d < 0:
    #    d = d % ((p-1)*(q-1))

    return (d, p * q)

def criptografa(mensagem, e, n):
    cript = []
    for c in mensagem:
        cript.append(pow(ord(c), e, n))

    return cript

def descriptografa(mensagem, d, n):
    decript = []
    for i in mensagem:
        decript.append(pow(i, d, n))

    return decript

#print(chavePrivada(17, 11, 13))
e, p, q = chavePublica(32)
d, n = chavePrivada(e, p, q)

a = criptografa("abacate", e, n)
print(descriptografa(a, d, n))
