import csv

class Students:
    all =[]
    def __init__(self,name: str,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
        
        #all new data will be stored in list
        Students.all.append(self)
        
        #getting data from csv file
    @classmethod
    def instantiate_from_csv(cls):
        #context manager 
        with open('first.csv','r') as f:
            reader = csv.DictReader(f);
            students = list(reader)

            for item in students:
                print (item)

    def __repr__(self):
        return f"\nStudents('{self.name}',{self.roll}, {self.section})"

# Student1 = Students("Posur",1,'A')
# Student2 = Students("Ransom",2,'B')
# Student3 = Students("ziri",3,'B')
# Student4 = Students("saico",4,'C')

# for Items in Students.all:
#     print(Items.name)

#if you want to print all data then you have to use repr method to print
# print(Students.all)

Students.instantiate_from_csv()



