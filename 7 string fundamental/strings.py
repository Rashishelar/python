
#string
p=print
s1='Generation'
print(s1)
s2="Generation"
print(s2)
s3="""Generation"""
p(s3)
s4='''Generation'''
p(s4)
p(s1,len(s1))
s5=[5]
p('indexing',s5)
s6=[8]
p(s6)
s7=s1[1:8]
p('slicing',s7)
s8=s1[2:10]
p(s8)
s9=s1[-10:-5]
p(s9)
s10=s1[-5:]
p(s10)
s11=s1[:]
p(s11)
s12=s1[-11:]
p(s12)


s13="""Everybody in this country learn, How to program a computer's"""
s14=(s13,len(s13))
p(s14)
s15=s13[10]
p('indexing',s15)
s16=s13[-5]
p('indexing',s16)
s17=s13[-14]
p('indexing',s17)
s18=s13[0:20]
p('slicing',s17)
s19=s13[:]
p(s19)
s20=s13[-20:-1]
p(s20)
