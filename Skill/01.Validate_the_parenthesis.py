s = input("Enter the String")
sl = len(s)
check = 0
o_sq, o_cur, o_par, c_sq, c_cur, c_par, = 0, 0, 0, 0, 0, 0
for i in range (0, sl):
    if s[i] == '(':
        o_par += 1
        continue
    elif s[i] == '{':
        o_cur += 1
        continue
    elif s[i] == '[':
        o_sq += 1
        continue
    elif s[i] == ')':
        o_par += 1
        continue
    elif s[i] == '}':
        o_cur =+ 1
        continue
    elif s[i] == ']':
        o_sq += 1
        continue
