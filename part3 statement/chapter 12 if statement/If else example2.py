basic_salary=int(input("Enter the basic_salary: "))
if basic_salary<1500:
    hra=basic_salary*(10/100)
    da=basic_salary*(90/100)
    total=basic_salary+hra+da
    print("Total salary: ",total)
else:
    hra=500
    da=basic_salary*(98/100)
    total=basic_salary+hra+da
    print("Total salary: ",total)
