a=int(input("Enter first number : "))
ch=input("Enter your character (+,-,*,/)  :  ");

if ch == '+':
    b=int(input("Enter second number : "))
    print("{} + {}  = ".format(a,b)+str(a+b));

elif ch == '-':
    b=int(input("Enter second number : "))
    print(" {} - {} = {}".format(a,b,a-b));

elif ch == '*':
    b = int(input("Enter Second Number : "))
    print(" {} x {} = {}".format(a,b,a*b));

elif ch == '/':
    b = int(input("Enter Second Number : "))
    print(" {} / {} = {}".format(a,b,a/b));


class duck:
    def walk(self):
        print("The duck is walking...")

    def sleep(self):
        print("the Duck is Sleeping...")


