mylist = ['Apple', 'Banana', 'Grape', 'Apple', 'Grape']
final=[]
for i in mylist:
    if i not in final:
        final.append(i)
print(final)