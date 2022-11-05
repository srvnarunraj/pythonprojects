mylist1=[18,2,3,6,5,6,6]
mylist2=[6,9,10,6,18]
final=[]
for i in mylist1:
    for j in mylist2:
        if i==j and i not in final:
            final.append(i)
mylist1.sort()
print(set(mylist1))
