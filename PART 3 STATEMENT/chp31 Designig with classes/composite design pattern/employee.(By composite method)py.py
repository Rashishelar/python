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
        return'[Employee:%s, %s, %s] '% (self.name,self.job,self.pay)

    
rashi=Employee('Rashi Shelar','dev',25000)
print(rashi)

class Manager:
    def __init__(self,name,pay):
        self.person=Employee(name,'Mgr',pay)
        
    def __getattr__(self,attr):
        return getattr (self.person,attr)

    def firstName(self):
        return self.name.split()[1]

    def middleName(self):
        return self.name.split()[1]

    def __repr__(self):
        return str(self.person)

dipti=Manager('Dipti shah',50000)
print(dipti)
