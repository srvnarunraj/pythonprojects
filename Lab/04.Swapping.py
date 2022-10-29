x = int(input("Enter x value : "))
y = int(input("Enter y value : "))


def withoutVariable(x , y):
    x += y
    y = x - y
    x = x - y
    print("Without Variables")
    print("Value of x is:  ", x, "  Value of y is : ", y)


def withVariable(x , y):
    t = x
    x = y
    y = t
    print("Using Variables")
    print("Value of x is:  ", x, "  Value of y is : ", y)

withoutVariable(x,y)
withVariable(x,y)