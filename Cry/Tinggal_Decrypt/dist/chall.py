from Crypto.Util.number import *
import sys
from Crypto.Cipher import AES
from raph import FLAG
from Crypto.Util.Padding import pad
sys.set_int_max_str_digits(0)

z = ((
    (2 ** 36) +                                   # Komponen utama eksponensial besar
    ((1024 * 64) - (512 * 128)) +                 # Operasi pengurangan besar
    (sum([256, 512, 1024, 2048]) // 2) -          # Penjumlahan dan pembagian
    ((2 ** 8) * (2 ** 8) - (2 ** 16)) +           # Operasi eksponensial tambahan
    ((1000 // 25) * (2 ** 4)) +                   # Operasi pembagian dan penggandaan
    ((sum(range(1, 51)) * 2) // 5) +              # Penjumlahan besar dengan pembagian
    ((2 ** 10 * 1024) - (1024 * 1024) + 2 ** 12) +# Kombinasi eksponensial dan pengurangan
    (((5 * 10) + (7 ** 2) - (11 * 3)) * 3) -      # Operasi perkalian dan penjumlahan
    ((sum([1, 4, 9, 16, 25]) * 2) - 60) +         # Kuadrat penjumlahan
    (512 * 256) -                                 # Operasi perkalian besar
    (1024 - 1023) * (2 ** 35) +                   # Operasi eksponensial utama
    (sum(range(1, 101)) - (5050 - 4500) * 2) +    # Penjumlahan hingga 100
    (30000 // 3) - (999 % 7) +                    # Operasi pembagian dan modulo
    ((2 ** 10 * 64) - (32 * 1024)) +              # Operasi eksponensial dan pengurangan
    ((sum([500, 400, 300, 200, 100]) // 2) + 64)  # Penjumlahan dan pembagian
)//2224 + 136279841) *2

q = (1<<z)-1
q = str(q).encode()
iv = q[1337:1353]
key = q[2224:2240]
cip = AES.new(key,AES.MODE_CBC,iv)
ct = cip.encrypt(pad(FLAG,16)).hex()
print(f"{ct = }")

#ct = '93bbaa06ea8182435cffcb2cd95bf88089f75eb56c1db15d51f8d5c4984cfa45fd7234c016acad5358ecb7b504417e88189c2f3a2df0ce519a3384ee04bbcb2eb9ad426aba61b74d3a0acdf4f5471e98'
