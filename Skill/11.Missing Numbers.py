n = [1, 2, 15]
maxv=max(n)
minv=min(n)
for i in range(minv,maxv):
    if i not in n:
        print(i)