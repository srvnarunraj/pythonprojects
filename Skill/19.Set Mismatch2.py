from collections import Counter
n = [1, 2, 4, 4]
def setmismatch(n):
    c = Counter(n)
    d = Counter([*range(1,len(n)+1)])
    return [*(c-d),*(d-c)]
print(setmismatch(n))