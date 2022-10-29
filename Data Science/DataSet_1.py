import pandas as pds
#Data Frame -> Converts csv into Table
arr = {
    "Name": ["Arun", "Ajay", "Nayab"],
    "Roll": [75, 62, 56]
}
x=pds.DataFrame(arr)
x=pds.Series(arr)
# x=pds.Series(arr,index=[101,102,103])

print(x)
