# multiple inheritance -> 2 child class and more base class
#method chaining -> calling multiple methods sequentially..
class Parents1:
    alive = True

    def brake(self):
        print("Brakes Applied...")
        return self

    def gear(self):
      print("The gear is smooth")
      return self

class Parents2:
    alives=True

    def gear():
      print("The gear is smooth")

class Child1(Parents1):
    pass

class Child2(Parents2):
    pass

class Daughter(Parents1,Parents2): #multiple->properties
    pass

p1=Parents1()
p2=Parents2()

c1=Child1()
c2=Child2()
Daught=Daughter()

p1.brake().gear() #method chaining 

# but before method chaining you have to return self in class member function..
