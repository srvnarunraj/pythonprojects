def plusOne(digits):
    if digits[-1] < 9:
        digits[-1] = digits[-1] + 1
    else:
        if len(digits) == 1:
            digits = [1, 0]
        else:
            digits = plusOne(digits[:-1]) + [0]
    return digits


print(plusOne([2, 3, 9, 1]))
