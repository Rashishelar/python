import a,b

mul1=a.mul(-5,-9)
print('from a:',mul1)

mul2=b.mul(4,21)
print('from b:',mul2)

from a import mul as city
from b import mul as country

mul1=city(10,20)
print('city:',mul1)

mul2=country(10,20)
print('country:',mul2)
