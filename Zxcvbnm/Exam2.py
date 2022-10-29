class A:
    def m1(self, s:str)->int:
        mydict = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
        result = 0
        tmp = 0
        i = 0
        while i < len(s):
            tmp = mydict[s[i]]
            if (i + 1) < len(s) and mydict[s[i]] < mydict[s[i + 1]]:
                tmp = mydict[s[i + 1]] - mydict[s[i]]
                i = i + 1
            i += 1
            result += tmp
        return result


obj = A()
x = input("Roman Number: ")
print(obj.m1(x))
