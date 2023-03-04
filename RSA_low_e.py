# -*- codeing = utf-8 -*-
# @Time : 4/3/2023 10:32
# @Author: JSG
# @File: RSA_low_e.py
# @Software: PyCharm
from gmpy2 import *
from Crypto.Util.number import long_to_bytes

filename = ['Frame3', 'Frame8', 'Frame12', 'Frame16', 'Frame20']
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

for i in range(5):
    if e[i] != e[0]:
        print('指数不同')
        break
    elif e[i] == e[0] and i == 4:
        print('指数相同')
print('e =', e[0])


def CRT(n, c):
    M = 1
    sum = 0
    for i in n:
        M = M * i
    for i in range(5):
        sum += (M // n[i]) * (invert(M // n[i], n[i])) * c[i]
    return pow(sum, 1, M)


tmp = iroot(CRT(n, c), e[0])
tmp = hex(tmp[0])[2:]
number = int(tmp[16:24],16)
plain = long_to_bytes(int(tmp[-16:] , 16))
print(plain)







