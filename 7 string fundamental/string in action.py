s0='''
#string in action
p=print
s1='spam'
p(s1, len(s1))
s2='Microphone'
p(s2,len(s2))
p('_'*30)
s3=s1[2]
print('indexing')
p(s3)
s4=s1[0]
p(s4)
s5=s1[-1]
p(s5)
s6=s1[-2]
p(s6)
p('_'*40)
print('concate')
s7=s1 + s2
p(s7)
s8=s7,(len(s7))
p(s8)
print('slicing')
s9=s1[0:3]
p(s9)
s10=s1[-4:]
p(s10)
s11=s2[0:9]
p(s11)
s12=s2[:-5]
p(s12)
s13=s1[:]
p(s13)
s14=s2[:]
p(s14)
'''
print(s0)
