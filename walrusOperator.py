# := it makes work easier..

# without wlrus...
food=list()
while True:
    foods = input("Enter the items for list ( -> none for exit) : ")
    if foods == "none":
        break
    food.append(foods)

# with walrus

food=list()
while foods := input("Enter the items for list ( -> none for exit) : ") != "none" :
    food.append(foods)
print(food)

# it makes work easier

