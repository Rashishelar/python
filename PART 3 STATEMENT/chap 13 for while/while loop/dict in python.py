#dict in python

dict1={'name':'Rashi',
       'Age':18,
       'skill':['python','java','.net']
       }
a2=list(dict1.keys())
i=0
while i<len(a2):
    print(dict1[a2[i]])
    i=i+1
