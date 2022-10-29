# Valid Parentheses: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if
# the input string is valid. An input string is valid if: a . Open brackets must be closed by the same type of
# brackets. b. Open brackets must be closed in the correct order.
s = input("Please,Enter the string : ")
sn = len(s)
v = 0
ocb, ofb, osb, ocb1, ofb1, osb1 = 0, 0, 0, 0, 0, 0
for i in range(0, sn):
    if s[i] == '(':
        ocb = ocb + 1
        continue
    elif s[i] == '{':
        ofb = ofb + 1
        continue
    elif s[i] == '[':
        osb = osb + 1
        continue
    elif s[i] == ')':
        ocb1 = ocb1 + 1
        continue
    elif s[i] == '}':
        ofb1 = ofb1 + 1
        continue
    elif s[i] == ']':
        osb1 = osb1 + 1
        continue
if ocb == ocb1:
    if ofb == ofb1:
        if osb == osb1:
            v = 1
if v == 1:
    print("Valid")
else:
    print("In valid")
