try:
    num1=int(input("Enter the num1:"))
    num2=int(input("Enter the num2:"))
    result=num1/num2
    print(result)
except ZeroDivisionError as e:
    print(e)
finally:
    print("This is always run")
