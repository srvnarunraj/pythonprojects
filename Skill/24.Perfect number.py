def perfectnumber(n):
    ans = 0
    for i in range(1, n - 1):
        if n % i == 0:
            ans += i
    if ans == n:
        print("Perfect number ")
    else:
        print("Imperfect number")


x = int(input("Enter the number : "))
print(perfectnumber(x))
