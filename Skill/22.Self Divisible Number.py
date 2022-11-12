start = int(input("Enter the start number : "))
end = int(input("Enter the end number : "))
Sol = []


def isdivible(n):
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
        Sol.append(num)


for n in range(start, end + 1):
    isdivible(n)

print(Sol)
