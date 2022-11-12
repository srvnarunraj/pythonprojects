n = int(input("Enter the number : "))
mylist = []
num = n
while n > 0:
    x = n % 10
    n = n // 10
    mylist.append(x)
r = 0
for i in mylist:
    if num % i == 0:
        r += 1

if len(mylist) == r:
    print("True")
else:
    print("False")
