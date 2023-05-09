'''per=int(input("Enter the percentage:"))
if per>=75:
    print("A")
elif per>=60:
    print("B")
elif per>=40:
    print("C")
else:
    print("Fail")'''

print("Qualification")
print("1:post Graduation")
print("2:Graduation")
print()

print("Gender")
print("M:Male")
print("F:Female")
print()

gender=input("Enter the gender:")
Qualification=int(input("Qualification:"))
yrs=int(input("Enter the yrs:"))

if gender=='M'and Qualification==1 and yrs>=10:
    salary=15000
    print("salary:",salary)
elif gender=='M' and Qualification==2 and yrs>10:
    salary=10000
    print("salary:",salary)
elif gender=='M' and Qualification==1 and yrs<=10:
    salary=1000
    print("salary:",salary)
elif gender=='M' and Qualification==2 and yrs<=10:
    salary=7000
    print("salary:",salary)
elif gender=='F' and Qualification==1 and yrs>=10:
    salary=12000
    print("salary:",salary)
elif gender=='F' and Qualification==2 and yrs>=10:
    salary=9000
    print("salary:",salary)
elif gender=='F' and Qualification==1 and yrs<10:
    salary=10000
    print("salary:",salary)
elif gender=='F' and Qualification==2 and yrs<10:
    salary=6000
    print("salary:",salary)
