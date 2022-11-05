x = [1, 2, 3, 4, 5, 9]
duplicate = 0
for i in x:
    for j in x:
        if j == i:
            duplicate += 1
if duplicate != len(x):
    print("Duplicate exists")
else:
    print("No duplicate")
