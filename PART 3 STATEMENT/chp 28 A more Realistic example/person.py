class AttrDisplay:
    def gatherAttrs(self):
        attrs=[]
        for key in sorted (self._dict_):
            attrs.append('%s=%s'%(key,gatatter(self,key)))
        return ','.join(attrs)
    
    def __repr__(self):
        return'[&s:%s]'%(self._class_._name_,self.gatherAttrs())


class Person(AttrDisplay):
    def __init__(self,name,mobile,job='None',pay,add='None')
    self.name=name
    self.mobile=mobile
    self.job=job
    self.pay=pay
    self.add=add

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self,percent):
        self.pay=int(self.pay*(1+percent))


class Fresher(Person):
    def __init__(self,name,mobile,add,pay):
        person.__init__(self,name,mobile,add,'System Engineer',15000)

    def firstName(self):
        return self.name.split()[-2]

if __name__=='__main__':
    raju=Person(name='Raju',mobile=8956230147,add='parel')
    omkar=Person(name='omkar')
