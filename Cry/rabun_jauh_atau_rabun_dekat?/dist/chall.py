from Crypto.Util.number import *
from raph import i,l,o,v,e,u, FLAG
m = bytes_to_long(FLAG)
n = i*l*o*v*e*u
p = pow(m,65537,n)
p = pow(p, 2, n)
print(f'n = {n}')
print(f'p = {p}')
