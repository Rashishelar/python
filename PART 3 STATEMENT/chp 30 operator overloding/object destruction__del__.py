class Employee:
    def __init__(self,name,job=None,pay=0.0):
        self.name=name
        self.job=job
        self.pay=pay

    def __repr__(self):
        return '[Employee:%s,%s,%s ]'% (self.name,self.job,self.pay)

    def __del__(self):
        print('Goodbyee:',self.name)

rashi=Employee('Rashi Shelar','CEO',500000)
print(rashi)
rashi=10
print(rashi)
rashi=50
print(rashi)
