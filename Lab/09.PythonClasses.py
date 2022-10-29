class divisor:
    num1 = 0

    def __init__(self, num1):
        self.num1 = num1
        for i in range(1, self.num1 + 1):
            if self.num1 % i == 0:
                print(i)


num1 = int(input("Enter the value : "))
obj = divisor(num1)
