#formatting method

temp1='{2},{1},{0}'.format('Rashi','python','c++')
print(temp1)

temp2='{0},{1}'.format ('Rashi','django','python')
print(temp2)

temp3='name:{name},age:{age}'.format('python',name='Rashi',age=18,project='c++',)
print(temp3)

temp4='age:{age}'.format(name='Rashi',age=18,salary=15000)
print(temp4)

temp5='{food}'.format('python',motto='spam',food='Tacco')
print(temp5)

temp6='{},and {name}'.format('spam','aam',name='Rashi')
print(temp6)

temp7='{name},{0[age]},{1[2]}'.format({'name':'Rashi','age':18,'salary':10000},[85,95,99],name='ham',)
print(temp7)
