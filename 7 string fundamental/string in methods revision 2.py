#string in method
a1='online python compiler (interpreter) compiler run python online'
a2='Rashi shelar'
a3='12345678'
a4='abc123'

print(a1,len(a1))
print(a2,len(a2))
print(a3,len(a3))

a4=a1.capitalize()
print('capitalize',a4)
print()
a5=a1.upper()
print('upper',a5)
print()
a6=a1.lower()
print('lower',a6)
print()
a7=a5.isupper()
print('isupper',a7)
print()
a8=a6.islower()
print('islower',a8)
print()
a9=a2.title()
print('title',a9)
print()
a10=a2.center(50,'_')
print('center',a10)
print()
a11=a2.count('Rashi',0,20)
print('count',a11)
print()
a12=a2.startswith('Rashi')
print('startswith',a12)
print()
a13=a2.endswith('Rashi')
print('endswith',a13)
print()
a14=a3.isalnum()
print('isalnum',a14)
print()
a15=a4.isalpha()
print('isalpha',a15)
print()
a16=a3.isdecimal()
print('isdecimal',a16)
print()
a17=a3.isdigit()
print('isdigit',a17)
print()
a18=a3.isnumeric()
print('isnumeric',a18)
print()
a19=a9.istitle()
print('istitle',a19)
print()
a20=a1.find('python',0,)
print('find',a20)
print()
a21=a1.rfind('python')
print('rfind',a21)
print()
a22=a1.index('compiler')
print('index',a22)
print()
a23=a1.rindex('compiler')
print('rindex',a23)
print()
a24=a1.partition('online')
print('partition',a24)
a25=a1.rpartition('online')
print('rartition',a25)
print()
a26=a1.split(' ')
print('split',a26)
print()
a27=a1.rsplit(' ')
print('rsplit',a27)
print()
a28=a1.center()
