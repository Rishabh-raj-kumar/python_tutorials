#inheritance -> there is base class and derive class(parents and child)
class Animal:
     alive=True

     def self(self):
        print("This animal is eating...")

     def sleep(self):
        print("This Animal is sleeping..")

class Rabit(Animal):
    
    def flow(self):
        print("flow in the beats")
class Fab(Animal):
    
    def fabourate(self):
        print("you are fab")

Anim=Animal()
Rab=Rabit()
Fabour=Fab()

print(Anim.alive)
Rab.self()
Fabour.sleep()

Rab.flow()
Fabour.fabourate()