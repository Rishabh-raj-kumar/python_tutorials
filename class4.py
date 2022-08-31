#passing objects as argument..
class Car:

    color = None

class Bike:
    color=None

def changeColor(vehicle,color): #this function is not inside a class
        vehicle.color=color

car_1=Car()
car_2=Car()
bike_1=Bike()

changeColor(car_1,"white") #passes object
changeColor(car_2,"green")
changeColor(bike_1,"black") #function reusability

print(car_1.color)
print(car_2.color)
print(bike_1.color)