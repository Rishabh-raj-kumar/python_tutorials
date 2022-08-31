import time
count=4;
for i in range(9,0,-1):
    count=count-1
    for j in range(count):
        print(" ",end="")
    for k in range(1,i,1):
        print("*",end="")
        if i == 8:
            continue
    print()
    time.sleep(0.5)
