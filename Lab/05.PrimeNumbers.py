x = int(input("Enter the Lower Limit : "))
y=  int(input("Enter the Upper Limit : "))
for i in range(x,y):
    count=0
    for j in range (2,i):
        if (i % j )== 0:
            count+=1
            break
    if (count == 0 and i!=1):
        print(i)
