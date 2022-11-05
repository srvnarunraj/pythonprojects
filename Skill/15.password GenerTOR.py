import random as r

alpha1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha2 = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'
spc = '!@#$%^&*()'
a = "".join(r.sample(alpha1, 2))
b = "".join(r.sample(alpha2, 2))
c = "".join(r.sample(num, 2))
d = "".join(r.sample(spc, 2))
tot = a + b + c + d
password = "".join(r.sample(tot, 8))
print("your password is : ", password)
