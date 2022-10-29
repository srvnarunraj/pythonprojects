#List Creation
Hotel = ['Biriyani']
while 1:
    print("List of Food Items")
    print('1.Add the Food')
    print("2.Delete the Food")
    print("3.View")
    choice = int(input("Select the Option : "))
    if choice == 1:
        q = int(input("Enter the No. of Food items to add : "))
        for j in range(0, q):
            new_item = input("Add the Food name : ")
            Hotel.append(new_item)
    elif choice == 2:
        w = input("Enter the item to delete : ")
        Hotel.remove(w)
    elif choice == 3:
        print(Hotel)
