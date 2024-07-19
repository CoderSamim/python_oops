class student:

    school="milli mission"  #class(statics) variable

    def __init__(self,m1,m2,m3):
        self.m1=m1                 #instance variable
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):         #get method (fetch or access the data)
        return self.m1

    def set_m1(self,value):    #set method (set or update or modify the data)
        self.m1=value



s1=student(20,30,45)
s2=student(45,89,56)

print(s1.avg())
print(s2.avg())
