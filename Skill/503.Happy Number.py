def hpynum(k):
    p = 0
    while k > 0:
        n = k % 10
        p = p + (n * n)
        k = k // 10
    return p
for k in range(1, 100):
    hpynum(k)
    idv = hpynum(k)
    while idv != 1 and idv != 4:
        idv = hpynum(idv)
    if idv == 1:
        print(k)
