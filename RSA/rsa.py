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
	while p == q:
		q = geraPrimo(bits)

	e = random.randint(0, pow(2,16))
	while math.gcd(e, (p-1)*(q-1)) != 1:
		e = random.randint(0, pow(2,16))

	return (e, p, q)

def chavePrivada(e, p, q):
    d = extendedEuclidean(e, (p-1)*(q-1))[1]
    if d < 1:
        # print('burro')
        d = d + ((p-1)*(q-1))
    # print(d)

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
        decript.append(chr(pow(int(i), d, n)))

    return decript

def quebra_forcabruta(n):
	p = int(math.sqrt(n)) + 1

	if p % 2 == 0:
		p += 1

	while n % p != 0:
		p -= 2

	q = n // p

	return (p, q)

def G(x,c):
	return pow(x,2) + c

def pollard_rho(n):
	x = random.randint(1, n)
	c = random.randint(1, n)
	y = x
	p = 1

	while p == 1:
		x = G(x, c) % n
		y = G(G(y, c), c) % n
		p = math.gcd(abs(x-y), n)

	return (p, n // p)


def main():
	bits = 64
	msg = open("mensagem.csv", "r")
	encripted = open("cript.csv", "w")
	uncripted = open("uncript.csv", "w")
	e, p, q = chavePublica(bits)
	d, n = chavePrivada(e, p, q)
	a = criptografa(msg.read(), e, n)
	# msg.truncate(0)
	# print(msg.read())
	for i in a:
		encripted.write(str(i))
		encripted.write(' ')

	encripted.close()
	encripted = open("cript.csv", "r")
	c = encripted.read().split()
	print(c==a)
	print(a)
	print('\n')
	print('\n')
	print(c)


	b = descriptografa(c, d, n)
	print(b)
	for j in b:
		uncripted.write(str(j))
	msg.close()
	encripted.close()
	uncripted.close()

	print(d)
	print((p,q))
	print(pollard_rho(n))
	#print(quebra_forcabruta(n))


	# print(descriptografa(a, d, n))
	# print((p,q))
	# print(quebra_forcabruta(n, bits))


if __name__ == '__main__':
	main()
