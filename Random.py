import random

x=random.randint(1,5)
print(x)

myList=[1,2,"zen","men","len","den"]
y=random.choice(myList)
print(y)

#lets shuffle lists...
random.shuffle(myList)
print(myList)