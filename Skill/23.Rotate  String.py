s = "abced"
goal = "edabcb"
text = s
for i in range(0, len(s)):
    k = text[i]
    sl=slice(1,len(s))
    s = s[sl]
    s+=k
    if s == goal:
        print("Yes MATCHED the goal in the ",i,"Iteration")