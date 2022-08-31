#timer in python
import time

# for i in range(10,0,-1):
#     print(i)
#     time.sleep(0.5)#0.5second
# print("welcome")

#pattern
for i in range(5):
    for j in range(5):
        print("*",end="")#end is used to print in same line..
    print()#print in new line

name="123-456-789"
for i in name:
    if i == "-":
        continue
    print(i,end=" ")