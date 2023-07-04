class Employee:
    list1=[x for x in range(10)]
    def __init__(self,name,job=None,pay=0.0):
        self.name=name
        self.job=job
        self.pay=pay

    def lastName(self):
        return self.name.split()[-1]

    def add(self,a,b):
        return a+b

    def __repr__(self):
        return'[Employee:%s, %s, %s]' %(self.name,self.job,self.pay)

rashi=Employee('Rashi shelar','dev',50000)
print(rashi)


class Manager(Employee):
    def __init__(self,name,pay):
        Employee.__init__(self,name,'Mgr',pay)

    def firstName(self):
        return self.name.split()[0]

    def MiddleName(self):
        return self.name.split()[1]

dipti=Manager('Dipti shah',50000)
print(dipti)        
