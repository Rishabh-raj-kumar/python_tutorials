#to create function -> def is used

def hello():#create function
    print ("Hello")

hello() #create object

#2.passing arguments 
def numb(num,name):
    print(str(num) + " " + name) #in order to print number with string you have to use str

numb(20,"bro")

#3.returning arguments
def multiply(num1,num2):
    return num1*num2

x=multiply(5,6)
print(x);

#4.keyword arguments
def list(Fname,Lname):
    print("hello "+Fname+" "+Lname)

list(Fname="bruh",Lname="zedda");

#5.* arguments
def Arg(*gargs):#after giving asterisk(*) yuhh can insert many variables
    sum =0;
    for i in gargs:
        sum+=i;
    return sum

x=Arg(2,2,4,5)
print(x)

#6. **arguments -> it works as a dictionaries...
def func(**flar):
    for key,values in flar.items():
        print(key+" : "+values)

func(Fname="firm",Lname="cirm",Mname="chirm")