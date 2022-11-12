x = input("Enter the char : ")
mydict = dict(A='a', B='b', C='c', D='d', E='e', F='f', G='g', H='h', I='i', J='j', K='k', L='l',
              M='m',N='n',O='o',P='p',Q='q',R='r',S='s')
ans = ''
for i in x:
    if i not in mydict:
        ans += i
    else:
        ans += mydict[i]
print(ans)
