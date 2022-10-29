a, n, b = 0, 0, 1
k = int(input("Enter the Stair numbers: "))
while n < k:
    c = a + b
    a = b
    b = c
    print(c)
    n += 1
print("Total Possible outcomes : ", c)