try:
    num1=int(input("Enter tge num1:"))
    num2=int(input("Enter the num2:"))
    result=num1/num2
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print(result)
