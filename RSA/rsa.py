import math
import random

def extendedEuclidean(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		gcd, x, y = extendedEuclidean(b % a, a)
		return (gcd, y - b//a * x, x)

################################################################################
################################################################################
################################################################################
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
        # print(n)
        n += 2

    return n

def chavePublica(bits):
    p = geraPrimo(bits)
    q = geraPrimo(bits)

    e = random.randint(0, pow(2,16))
    while math.gcd(e, (p-1)*(q-1)) != 1:
        e = random.randint(0, pow(2,16))

    return (e, p, q)

def chavePrivada(e, p, q):
    d = extendedEuclidean(e, (p-1)*(q-1))[1]
    if d < 1:
        print('burro')
        d = d + ((p-1)*(q-1))
    print(d)

    return (int(d), p * q)

def criptografa(mensagem, e, n):
    cript = []
    for c in mensagem:
        cript.append(pow(ord(c), e, n))

    return cript

def descriptografa(mensagem, d, n):
    decript = []
    for i in mensagem:
        #print(pow(i, d, n))
        decript.append(chr(pow(i, d, n)))

    return decript

def quebra_forcabruta(n, bits):
    bits += 1
    for p in range(pow(2,bits)):
        if fermatPrimalityTest(p):
            for q in range(pow(2,bits)):
                if fermatPrimalityTest(q) and p * q == n:
                    return (p,q)

bits = 16
msg = open("mensagem.csv")

e, p, q = chavePublica(bits)

d, n = chavePrivada(e, p, q)
a = criptografa(msg.read(), e, n)
print(descriptografa(a, d, n))

print((p,q))
print(quebra_forcabruta(n, bits))
