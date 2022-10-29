# Errors in Python
# 1.Zero Division Error
# 2.Name Error
# 3.Input Error
# 4.EOF Error( End of File)
# try - Except
# java point -Exception Handling
x, y = int(input("Enter x value "))
# x, y = map(int, input().split())
try:
    print(x / y)
except Exception:
    print("Zero Division Error")
else:
    print("No exception")
finally:
    print("Execution Happened")
