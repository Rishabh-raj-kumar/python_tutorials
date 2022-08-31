
# age=int(input("Enter your age : "));

# if age >18:
#     print("You are adult...");
# else : 
#     print("You are a noob...");

# if age>18 and age<50:
#       print("you are an adult...")
# elif age >55:
#     print("Buddha");
# else : 
#     print("you are child...");

name ="";

while len(name) == 0 :
    name=str(input("Enter your name : "));

print("hello "+name);

temp=int(input("Enter your temperature : "));
if temp <0 or temp >-30:
    print("Very cold today...")
elif not(temp <0 and temp >30):
    print("Very hot today...")

names =None;

while not names:
    names=str(input("Enter your name : "));
print(names)

for i in range(5):
   print("*")

#(inclusive(start),exclusive(end));
#(start,end,condition);

for j in range(50,100):
    print("{}")

for k in range(4,8+1,2):
    print(k)
    

#itterate for loop in string;
fame="BioDiversity"
for namek in fame:
    print(namek);