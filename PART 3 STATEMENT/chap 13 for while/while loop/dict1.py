#dict in python

dict1={'name':'Rashi',
       'Age':18,
       'Phones':[8956231470,7894561230,12346567895]
       }
a2=list(dict1.keys())
i=0
while i<len(a2):
    print(dict1[a2[i]])
    i=i+1
