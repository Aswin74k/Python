class car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def displayDetails(self):
        print("Brand:",self.brand)
        print("Model:",self.model) 
        print("Price:",self.price)  
c1 = car("BMW","X5","9600000")  
c1.displayDetails()         

class student:
    def __init__(self,Studentname,rollnumber,mark):
        self.Studentname = Studentname
        self.rollnumber = rollnumber
        self.mark = mark
    def displayDetails(self):
        print("Student name:",self.Studentname)
        print("Roll number:",self.rollnumber)
        print("Mark:",self.mark)
c1 = student("Aswin","rollnumber","mark")
c1.displayDetails()

