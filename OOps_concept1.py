
class Item:
    #constructor in python..
    #def __init__(self,name):
        # write f to format variable in print
        #print(f"I am a creator of {name}")
    
    #iniatilizing constructors..
    # def __init__(self,name: str,phone,roll):
    #     self.name=name;
    #     self.phone=phone;
    #     self.roll=roll;
    #method of class
    def __init__(self,name: str,price: float,quantity=0):
        #RUN validation to the received arguments
        #if price >= 0 then ok , else throw error..
        assert price >= 0, f"Price {price} is greater then zero!"
        #assert  condition,    error.
        assert quantity >=0 ,f"Quantity {quantity} is not greater than zero!"

        self.name=name;
        self.price=price;
        self.quantity=quantity;

    def calculate_total_price(self):
        return self.price * self.quantity 
    
    # def display(self):
    #     print(f"Your name : {self.name}");
    #     print(f"Your Phone Number : {self.phone}");
    #     print(f"Your roll Number : {self.roll}");

    def display_rate(self):
        return self.price * self.pay_rate


Item1 = Item("Phone",21,210);
# Item1.display()

print(Item1.calculate_total_price());
print(Item1.__dict__);#Show all the item in dictionary format
#accessing class attributes...
Item1.pay_rate = 0.7
print(Item1.display_rate());