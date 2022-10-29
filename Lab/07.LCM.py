x = int(input("Enter the num1 : "))
y = int(input("Enter the num2 : "))
z = int(input("Enter the num3 : "))
# check the greater Number among them
a = x if x > y else y
b = a if a > z else z
while 1:
    if b % x == 0 and b % y == 0 and b % z == 0:
        print(b)
        break
    b += 1