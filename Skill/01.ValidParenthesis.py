def isValid(s) -> int:
    stack = []
    paran_list = {')': '(', '}': '{', ']': '['}
    if s[0] in paran_list:
        print('arun1')
        return -1
    for i in s:
        if i not in paran_list:
            stack.append(i)
        else:
            if len(stack) == 0:
                print('arun')
                return -1
            temp = stack.pop()
            if paran_list[i] != temp:
                return 1                             #{[(]})
            # { [ ( ) ] }
    return 1 if len(stack) == 0 else -1

a = input("Enetr the parantheses : ")
b = isValid(a)
if b == 1:
    print('valid')
else:
    print('invalid')