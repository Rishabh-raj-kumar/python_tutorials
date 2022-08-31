#multi-level inheritance -> first derived class takes property of first derived class

class Base:

    alive = True

class Derived1(Base):

    def alim(self):
        print("so true words...")

class Derived(Derived1):

    def der():
        print("This class is double derived..")

bss=Base()
deri=Derived1()
deries=Derived()

print(deri.alive)
deries.alim()