import p,q

add1=p.f1(9,8)
print('from p:',add1)

add2=q.f1(8,8)
print('from q:',add2)

from p import f1 as Hello
from q import f1 as Hey

add1=Hello(9,3)
print('Hello:',add1)

add2=Hey(3,7)
print('Hey:',add2)
