#tuples ..collection which is ordered and unchangeable
#            used to group together the related data

sins = ("bro",31,"mal")
print(sins)

#count how many time value appeared
print(sins.count("bro"))

#get index
print(sins.index("bro"))

#set -> it is a collection which is unordered and unindexed.(no duplicate value);

utensils={"bartan","jhartan","tartan"}
print(utensils)

#adding elements in sets
utensils.add("ghartan")
print(utensils)

#removing elements in sets
utensils.remove("bartan")
print(utensils)

# #updating elements in sets(adding more)
dishes={"mongo","longo","chongo"}
# dishes.update(utensils)
# print(dishes)

#union in sets...
dinner=dishes.union(utensils)
for x in dinner:
    print(x)
print("******")

#not union in sets...
dinner=dishes.difference(utensils)
for x in dinner:
    print(x)

print("******")

#common in both...
dinner=dishes.intersection(utensils)
for x in dinner:
    print(x)