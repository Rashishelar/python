number=int(input("Enter the number:"))
if number%2==0:
    if number%4==0:
        print("Even number is divisible by 4 ")
    else:
        print("Even number is not divisible by 4")
else:
    if number%3==0:
        print("Odd number is divisible by 3")
    else:
        print("Odd number is not divisible by 3")
