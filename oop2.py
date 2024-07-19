class student:

    school="milli mission"  #class(statics) variable

    def __init__(self,m1,m2,m3):
        self.m1=m1                 #instance variable
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3


    @classmethod
    def get_school(cls):       #class method
        return cls.school



    @staticmethod
    def info():
        print('this is a static method')


s1=student(20,30,45)
s2=student(45,89,56)

print(s1.get_school())
print(student.get_school())

print(s2.avg())


print(s2.info())
print(student.info())


