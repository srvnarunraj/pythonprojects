k = int(input("Enter the Integer: "))
binvalue = bin(k)
x = binvalue.count("1")
print(x)

# Method 2
k = int(input("Enter the Integer: "))
print(bin(k).count("1"))
