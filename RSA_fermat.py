# -*- codeing = utf-8 -*-
# @Time : 4/3/2023 12:50
# @Author: JSG
# @File: RSA_fermat.py
# @Software: PyCharm
import binascii

from gmpy2 import *

with open("Frame10") as f:
    frame = f.read()
f.close()
n = int(frame[:256], 16)
e = int(frame[256:512], 16)
c = int(frame[512:], 16)

a = iroot(n, 2)[0]
'''
由于开方的时候会向下取整，所以这里对a进行手动加一
'''
a += 1
while True:
    if iroot((a ** 2 - n), 2)[1] == 1:
        b = iroot((a ** 2 - n), 2)[0]
        break
    a += 1
p = a + b
q = a - b
fai = (p - 1) * (q - 1)
d = invert(e, fai)
m = powmod(c, d, n)
print(binascii.a2b_hex(hex(m)[-16:]))
