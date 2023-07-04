class Person:
    def __init__(self,name,job=None,pay=0.0):
        self.name=name
        self.job=job
        self.pay=pay

    def giveRaise(self,percent):
        self.pay=int(self.pay+self.pay*percent)

    def lastName(self):
        return self.name.split()[-1]

    def __repr__(self):
        return '[Person:%s,%s,%s]' %(self.name,self.job,self.pay)

class Manager:
    def __init__(self,name,pay):
        self.person=Person(name,'Mgr',pay)

    def __getattr__(self,attr):
        return getattr (self.person,attr)

    def giveRaise(self,percent,bonus):
        self.person.giveRaise(percent+bonus)
    
    def firstName(self):
        return self.name.split()[0]

    def middleName(self):
        return self.name.split()[1]

    def __repr__(self):
        return str(self.person)
   

rashi=Manager('Rashi Rajesh Shelar',50000)
print(rashi)

