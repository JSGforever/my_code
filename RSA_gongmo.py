# -*- codeing = utf-8 -*-
# @Time : 4/3/2023 10:10
# @Author: JSG
# @File: RSA_gongmo.py
# @Software: PyCharm

from gmpy2 import invert, powmod
import binascii

with open("Frame0") as f:
    f1 = f.read()
f.close()

with open("Frame4") as f:
    f2 = f.read()
f.close()

n0, e0, c0 = int(f1[:256], 16), int(f1[256:512], 16), int(f1[512:], 16)
n4, e4, c4 = int(f2[:256], 16), int(f2[256:512], 16), int(f2[512:], 16)


def RSA_gongmo_attack(N, e1, e2, c1, c2):
    d1 = invert(e1, e2)
    d2 = (d1 * e1 - 1) // e2
    true_c2 = invert(c2, N)
    return (powmod(c1, d1, N) * powmod(true_c2, d2, N)) % N


if n0 == n4:
    ans = RSA_gongmo_attack(n0, e0, e4, c0, c4)
    answer = binascii.a2b_hex(hex(ans)[2:])
    print(answer[-8:])

