def adddigit(n):
    sums = 0
    while n > 0:
        k = n % 10
        sums += k
        n //= 10
    print("len is ", len(str(sums)), sums)
    if len(str(sums)) > 1:
        adddigit(sums)
    return sums


n = int(input("Enter the input: "))
print("Endvalue:  ", adddigit(n))