# DOB Calculator
# name = input("Enter your name : ")
dob: int = int(input("Enter your DOB (xx:xx:xxxx): "))
year = dob % 10000
dob = dob // 10000
month = dob % 100
dob = dob // 100
date = dob
result = ("DOB is : ", 2022 - year, "year", 9 - month, "months", dob-5, "days")
if month == 1 or month ==  3 or month ==  5 or month == 7 or month == 8 or month == 10 or month == 12 and date <= 31:
    print("1", result)

elif ((month == 4 or month == 6 or month == 9 or month == 11) and date < 30):
    print("2", result)

elif month == 2 and date <= 28:
    print("3", result)
else:
    print("Invalid Date")
