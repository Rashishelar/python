    #tuples
tuple1=()
print('tupel1',tuple1,len(tuple1))
tuple2=(10,20,30,40,50)
print('tuple2',tuple2,len(tuple2))
tuple3=(
        1,2,3,20.50,
        'RASHI SHELAR',
       {
            'name':'Rashi shelar',
            'skils':['.net','python','c++'],
        },
        (50.66,99,89.56),
        [1,2,5,6,80.99]
 )
print('tuple3',tuple3,len(tuple3))
tuple4=(8,7,9,5,5,5,58)
print('tuplel4',tuple4,len(tuple4))

print()
print('index')
a1=tuple2[-3]
print(a1)
print()

print('slicing')
a3=tuple4[1:4]
print(a3)
a4=tuple3[-3:-1]
print(a4)

print()
print('concate')
tuple5=tuple3+tuple4
print(tuple5)
tuple6=tuple2+tuple4
print(tuple6)

print()
print('concate')
tuple7=tuple2*2
print(tuple7)
tuple8=tuple4*5
print(tuple8)

print()
print('count')
a5=tuple8.count(5)
print(a5)
a6=tuple8.count(1)
print(a6)

print()
print('index')
a7=tuple8.index(5)
print(a7)
a8=tuple8.index(5)
print(a8)
