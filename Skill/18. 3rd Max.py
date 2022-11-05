k = [2, 1]
k.sort()
n = list(set(k))
if len(n) > 3:
    print(n[-3])
else:
    print(max(n))
