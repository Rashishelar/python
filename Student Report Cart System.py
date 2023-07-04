import colorama
from colorama import Fore
colorama.init()

print('\t\tStudent Report-Cart System')
print('-'*25,'Input Section','-'*25)
std_dict={}
total=0.0
student_name=input('Name:\n')
std_dict['student_name']=student_name
print()

school_name=input('School Name:\n')
std_dict['school_name']=school_name
print()

JAVA=int(input('Enter Java Marks out of 100:\n'))
std_dict['JAVA']=JAVA
total=total+JAVA
print()

CPP=int(input('Enter C++ Marks out of 100:\n'))
std_dict['C++']=CPP
total=total+CPP
print()

JSP=int(input('Enter JSP Marks out of 100:\n'))
std_dict['JSP']=JSP
total=total+JSP
print()

PYTHON=int(input('Enter Python Marks out of 100:\n'))
std_dict['PYTHON']=PYTHON
total=total+PYTHON
print()

JAVASCRIPT=int(input('Enter JavaScript Marks out of 100:\n'))
std_dict['JAVASCRIPT']=JAVASCRIPT
total=total+JAVASCRIPT
print()

GO=int(input('Enter GO Marks out of 100:\n'))
std_dict['GO']=GO
total=total+GO
print()

list1=[]
for key in std_dict:
    if isinstance(std_dict[key],int):
       list1.append(len(key))
       
list1.sort(reverse=True)

print()
print()
print('-'*25,'Output Section','-'*25)
print()
print()
print(Fore.RED+'School:',std_dict['school_name'])
print()
print('Student:',std_dict['student_name'])
print()
print('Total:',total)
for key in std_dict:
    if isinstance(std_dict[key],int):
        if std_dict[key]>=20.00 and std_dict[key]<=49.99:
            key_len=list1[0]-len(key)
            print(key+' '*key_len,'\t='+str(std_dict[key])+'/100','\t-Grade C')
            print()
        elif std_dict[key]>=50.00 and std_dict[key]<=74.99:
            key_len=list1[0]-len(key)
            print(key+' '*key_len,'\t='+str(std_dict[key])+'/100','\t-Grade B')
            print()
        elif std_dict[key]>=75.00:
            key_len=list1[0]-len(key)
            print(key+' '*key_len,'\t='+str(std_dict[key])+'/100','\t-Grade A')
            print()
        else:
            key_len=list1[0]-len(key)
            print(key+' '*key_len,'\t='+str(std_dict[key])+'/100','\t-Grade D')
            print()
        
print('-'*50)
print('Total= ',total)
per=int(total/600*100)
print('Percentage= ',str(per)+'%')
if per>=20.00 and per<=49.99:
    print('Overall Grade= ','C')
elif per>=50.00 and per<=74.99:
    print('Overall Grade= ','B')
elif per>=75.00:
    print('Overall Grade= ','A')
else:
    print('Overall Grade= ','D')    
