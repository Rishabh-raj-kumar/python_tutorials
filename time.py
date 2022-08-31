import time

print(time.ctime(time.time())) #gives exact date and time..

#-----------OR------------->

doc = time.localtime();
local=time.strftime("%B %d %Y %H:%M:%S",doc)
print(local)