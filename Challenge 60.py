#Curtis Lincoln
#Challenge 60

File = open("ShoppingList.txt", "w")
Item = ""
Shopping_List = []
while Item != "STOP":
    Item = input("What item do you want to add to the shopping list?: ")
    if Item != "STOP":
        Shopping_List.append(Item)
for Items in Shopping_List:
    File.write(Items)
    File.write("\n")

File.close()
File = open("ShoppingList.txt", "r")
print(File.read())
