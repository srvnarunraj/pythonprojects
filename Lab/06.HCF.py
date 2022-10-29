x = int(input("Enter the num1 : "))
y = int(input("Enter the num2 : "))
# check the greater Number among them
a = x if x > y else y
print("Factors are: ")
# Verify the Factors
for i in range(1, a + 1):
    if x % i == 0 and y % i == 0:
        result = i
        print(i)
print("HCF is : ",result)


