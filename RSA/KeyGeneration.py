# INPUT: Required modulus bit length, k.
# OUTPUT: An RSA key pair ((N,e),d) where N is the modulus, the product of two primes (N=pq) not exceeding k bits in length; e is the public exponent, a number less than and coprime to (p−1)(q−1); and d is the private exponent such that ed≡1mod(p−1)(q−1).
# Select a value of e from 3,5,17,257,65537
# repeat
#    p ← genprime(k/2)
# until (pmode)≠1
# repeat
#    q ← genprime(k - k/2)
# until (qmode)≠1
# N ← pq
# L ← (p-1)(q-1)
# d ← modinv(e, L)
# return (N,e,d)
