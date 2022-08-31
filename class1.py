class Car:

    #creating cunstructor..
    def __init__(self,name,model,type):
        self.name = name
        self.model = model
        self.type=type

    #creating member functions...
    def drive(self):
        print("This car is driving self..")

    def stop(self):
        print("The Car Stopped...")

