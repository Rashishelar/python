#addd

add=lambda x,y:x+y
print(add(10,25))

#sub

sub=lambda x,y:x-y
print(add(-15,20))

#multiply

mul=lambda x,y:x*y
print(mul(-55,21))

#div

div=lambda x,y:x/y
print(div(5,2))

#mod

mod=lambda x,y:x%y
print(mod(2,9))

#lower

lower=(lambda a,b:a if a<b else b)
print(lower(20,10))

#list1_map

list1=(4,5,6,7,8,98)
list_map=list(map(lambda x:x/2,list1))
print(list_map)

#list2_filter

list2=[2,4,6,8,12,47,69,18,20]
list_filter=list(filter(lambda x:x%2==0,list2))
print(list_filter)
