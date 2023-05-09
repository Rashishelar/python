'''number=int(input("Enter the number:"))
if number%2==0:
    if number%4==0:
        print("Even number it is %4")
    else:
        print("even number is not %4")
else:
   
    if number%3==0:
        print("Odd number is %3")
    else:
        print(" odd number is not divisible %3")'''

per=int(input("Enter the percentage:"))
if per>=75:
    print("A")
else:
    if per>=60:
        print("B")
    else:
        if per>=40:
            print("C")
        else:
            print("Fail")
    
