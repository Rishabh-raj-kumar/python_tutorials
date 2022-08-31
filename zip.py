# zip(*iterables) -> aggregate elements from two or more iterables(list,tuples,dict,sets)..

username = ["dude","zude","fude"]
valu = ["password","wired","fired"]

users = zip(username,valu)

#converting in tuple...
for i in users:
    print(i)

print()
#converting in dictionary...
nusers=dict(zip(username,valu))

for key,value in nusers.items():
    print(key+" : "+value)
