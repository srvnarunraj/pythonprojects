n = ["A", "R", "U", "N"]
i = 0
j = len(n)-1
while i < j:
    n[i], n[j] = n[j], n[i]
    i += 1
    j -= 1
print(n)
