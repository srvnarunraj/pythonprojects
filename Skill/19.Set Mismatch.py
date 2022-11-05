n = [1, 2, 4, 4]
n.sort()
p = list(set(n))
sol = []
for i in range(0, len(n)):
    try:
        if p[i] != n[i]:
            sol.append(n[i])
            break
    except:
        sol.append(n[i])
for i in range(min(n), max(n)):
    if i not in n:
        sol.append(i)
print(sol)
