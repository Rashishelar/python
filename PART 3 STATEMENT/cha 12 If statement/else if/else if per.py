m1=int(input("Enter the number m1: "))
m2=int(input("Enter the number m2: "))
m3=int(input("Enter the number m3: "))
m4=int(input("Enter the number m4: "))
m5=int(input("Enter the number m5: "))

per=(m1+m2+m3+m4+m5)/500*100
if per>75:
    print("A")
elif per>60:
    print("B")
elif per>=40:
    print("C")
else:
    print("Fail")
    
