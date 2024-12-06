from Crypto.Util.number import *
from functools import reduce
import itertools
from sage.all import ecm
def square_root(a, p):
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return 0
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def legendre_symbol(a, p):

    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls

def crt(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)

    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def decryption(c, p, q, r,s,t,u):
    output = []
    n = [ p, q, r,s,t,u ]
    m_p, m_q, m_r,m_s,m_t,m_u = 0, 0, 0,0,0,0
    m_p = square_root(c,p)
    m_q = square_root(c,q)
    m_r = square_root(c,r)
    m_s = square_root(c,s)
    m_t = square_root(c,t)
    m_u = square_root(c,u)

    congruence_system = [[m_p,p-m_p], [m_q,q-m_q], [m_r,r-m_r], [m_s,s-m_s],[m_t,t-m_t],[m_u,u-m_u]]
    for i in list(itertools.product(*congruence_system)):
        output.append((crt(n, list(i))))
    return output
n = 3592511758607706080877373445462315283097617620126489133600265910584253818474695911554142865076810521355771073332795449335961895193547635196519520994685338235627790171836809
A = 1738228029934314978434052027727772755821546791813849877308430846830480907799305799420078867384952263052163556913097904777074735845294691359339706310922203672796193002734107

p,q,r,s,t,u = ecm.factor(n)
      
der = decryption(A,p,q,r,s,t,u)
print(der)
n = p*q*r*s*t*u
phi_n = (p - 1) * (q - 1) * (r - 1) * (s - 1) * (t - 1) * (u - 1)
e = 65537
d = inverse(e, phi_n)
for i in der:
    decrypted = long_to_bytes(pow(i, d, n))
    if b'NEXUS' in decrypted:
        print("Found match:", decrypted.decode('latin-1'))
