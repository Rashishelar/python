"""
#product

cost_price=int(input("Enter the  cost price :"))
selling_price=int(input("Enter the selling price:"))
if selling_price>cost_price:
    profit=selling_price-cost_price
    print("profit",profit)
else:
    loss=selling_price-cost_price
    print("Loss",loss)
"""
"""       
#salary

basic_salary=int(input("Enter the basic_salary:"))
if basic_salary<1500:
        HRA=basic_salary*(10/100)
        DA=basic_salary*(90/100)
        total=basic_salary+HRA+DA
        print("Total salary :",total)
else:
    HRA=500
    DA=basic_salary*(98/100)
    total=basic_salary+HRA+DA
    print("Toatl salary:",total)
"""

#student

percent=int(input("Enter the student percent:"))
if percent >=80:
    print("First class")
else:
    print("Second class")

    

percent=int(input("Enter the student percentage:"))
if percent<35:
    print("Fail")
else:
    print("Pass")

