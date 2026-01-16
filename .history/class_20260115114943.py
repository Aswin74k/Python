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
    def __init__