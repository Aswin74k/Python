amount = int(input("Enter purchase amount:"))
if amount > 1000: 
    discount = amount * 10 / 100
    final_discount = amount - discount
    print("10 % discount applied")
    print("final amount",finlal_amount)
else: 
    print("No discount") 
    print("final amount",amount)   



age = int(input("Enter age")) 
if age < 13: 
    print("child")
elif       