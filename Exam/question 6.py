class Student():
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def display_name(self):
        return self.name

    def display_age(self):
        return self.age

    def display_marks(self):
        return self.marks

s1=Student('Rashi Shelar',18,700)
name=s1.display_name()
print(name)
age=s1.display_age()
print(age)
marks=s1.display_marks()
print(marks)
