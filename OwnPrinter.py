
# passing print in variable
Adity = print
Adity("I love you😘")

# passing function inn variable

def hello():
    Adity("hi Adity..")

pandey=hello
pandey()

#Higher Order Function...
#1. accept a function as argument..

def total(num):
    return num;

def name(nam):
    return nam.upper()

def hello(text):
    names=text("hello") #hello.upper()
    print(names)        

# The hello function will take other function as argument and return  its returning points
hello(total)
hello(name)

#2. return a function..
#(In a python function are also treated as objects)

def divisor(x):
    def dividend(y):
        return x/y;
    return dividend  #returning a function

divide=divisor(9)  #1. passing value to divisior
print(divide(9))   #2.passing value to diviends