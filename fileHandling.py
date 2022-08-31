import os
import shutil

path="try1.txt"

if os.path.exists(path):
    print ("Exists")
else :
    print("file not found")

#read files..
with open('try1.txt') as file:
    print(file.read())

#write in file..
name="Dhoom Machale \nCradle"
with open('try1.txt','w') as file:
    file.write(name);

#copy file..
shutil.copy2('try1.txt','try2.txt')

#delete file with python...
phat='try2.txt'
os.remove(phat)