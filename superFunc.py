#super() -> function used to gives access to the methods of parents class

class Rectangle:

    def __init__(self,x,y):
        self.x=x
        self.y=y
        #dont change variable while initailizing..

class Square(Rectangle):

    def __init__(self,x,y):
     super().__init__(x,y) #accessing parents class constructor..

    def area(self):
        return self.x*self.y

class Cube(Rectangle):

    def __init__(self,x,y,k):
        super().__init__(x,y)
        self.k=k
    
    def volume(self):
        return self.x*self.y*self.k

Squa=Square(3,3)
cube=Cube(3,3,3)

print(Squa.area())
print(cube.volume())
