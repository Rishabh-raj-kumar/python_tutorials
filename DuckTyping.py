#duck typing -> concept where the class of an object is less importnt than methods...
import time

class Duck:
     def walk(self):
        print("Duck is walking..")

     def sleep(self):
        time.sleep(1)
        print("Now Duck is sleeping...")

class Person:

    def catch(self,duck):
        duck.walk()
        duck.sleep()
        time.sleep(1)
        print("And You catched the duck 😒")

duck=Duck()
Persons=Person()

Persons.catch(duck) #catch the object and insert it in second class method