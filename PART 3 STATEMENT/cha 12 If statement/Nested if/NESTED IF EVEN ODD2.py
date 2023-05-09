'''number=int(input("Enter the number:"))
if number%2==0:
    print("Even number")
else:
    print("Odd number")'''


'''number=int(input("Enter the number:"))
if number%2==0:
    if number%4==0:
        print("Even number and divisible by 4")
    else:
        print("Even number is not divisble by 4")
else:
    if number%3==0:
        print("Odd number and divisble by 3")
    else:
        print("odd number is not divisble by 3")'''


list1=[20,89.99,['Rashi','Shelar'],99999,1e-4]
print("list1",list1,len(list1))


dict2={
    'name':'Rashi',
    'ID':9898,
    'Phone':9874563210,
    'Age':18,
    'skill':'python'
    }
print("dict1",dict2,len(dict2))


t3=(895623,123,1e-89,4,20.80,9.99,23015)
print("t3",t3,len(t3))

sets={1,2,2,3,4},{6,7,7,7,9,},{9,8,6,5,3,2}
print("sets",sets,len(sets))
