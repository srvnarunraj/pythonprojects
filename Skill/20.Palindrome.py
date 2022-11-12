def palindrome(x):
    xrev=""
    for j in x[::-1]:
        xrev+=j
    if xrev == x:
        return True



x = input("Enter the text : ")

print(palindrome(x))
