total_student=int(input("Total student:"))
student_no=1
while student_no < total_student:
    print("student No",student_no)
    name=input("Enter the student name: ")
    cls=input("Enter the class name:")
    m1=int(input("Enter the marks m1:"))
    m2=int(input("Enter the marks m2:"))
    m3=int(input("Enter the marks m3:"))
    m4=int(input("Enter the marks m4:"))
    m5=int(input("Enter the marks m5:"))
    m6=int(input("Enter the marks m6:"))
    total=m1+m2+m3+m4+m5+m6
    print("total:",total)
    per=total/750*100
    print("per:",per)


    if per>75:
        print("A")
    elif per>60:
        print("B")
    elif per>50:
        print("c")
    elif per>40:
        print("D")
    else:
        print("F")
    student_no = student_no+1
