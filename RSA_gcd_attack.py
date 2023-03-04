# -*- codeing = utf-8 -*-
# @Time : 4/3/2023 11:49
# @Author: JSG
# @File: RSA_gcd_attack.py
# @Software: PyCharm
from gmpy2 import *
import binascii
filename = ['Frame1', 'Frame18']
frames = []
for i in filename:
    with open(i) as f:
        frames.append(f.read())
    f.close()
n = []
c = []
e = []
for i in frames:
    n.append(int(i[:256], 16))
    e.append(int(i[256:512], 16))
    c.append(int(i[512:], 16))

if gcd(n[0], n[1]) > 1:
    print("存在公因数")
p = gcd(n[0], n[1])
q1 = n[0] // p
q18 = n[1] // p
fai1 = (p - 1) * (q1 - 1)
fai18 = (p - 1) * (q18 - 1)
d0 = invert(e[0], fai1)
d18 = invert(e[1], fai18)
m1 = pow(c[0], d0, n[0])
m18 = pow(c[1], d18, n[1])
plaintext1 = binascii.a2b_hex(hex(m1)[2:])[-8:]
plaintext18 = binascii.a2b_hex(hex(m18)[2:])[-8:]
print("plaintext1 =", plaintext1)
print("plaintext18 =", plaintext18)


