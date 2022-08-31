#lists in python...used to store multiple items in single variable

food=["zem","mem","tem","lem"]
print (food)

#replace elements

food[0]="shusi"
print (food[0])

#adding new elements
food.append("zener");
food.append("lesser")
print (food)

#remove element in lists..
food.remove("shusi")

#remove last element in lists..
food.pop();

#insert element in lists with position..
food.insert(5,"shusi")
print (food)

#sort the list..
food.sort()
print(food)

#clear all the elements in lists..
food.clear()
print(food)

#2D lists = list of lists..

foods=["ham","cam","jam"]
soda=["coka","maja","sprite"]
lists=[foods,soda]
print(lists)

#accessing 2D lists with index..
print(lists[0][2])