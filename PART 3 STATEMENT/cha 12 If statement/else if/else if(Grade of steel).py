hardness=int(input("Enter the hardness:"))
carbon=float    (input("enter the carbon:"))
Tensile=int(input("Enter the Tensile"))

if hardness>50 and carbon<1 and Tensile>5600:
    print("grade 10")
elif hardness>50 and carbon<1:
    print("grade 9")
elif carbon<1 and Tensile>5600:
    print("grade 8")
elif hardness>50 and Tensile>5600:
    print("grade 7")
elif hardness>50 or carbon<1 or Tensile>5600:
    print("grade 6")
else:
    print("grade 5")
