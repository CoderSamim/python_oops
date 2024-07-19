class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

        self.lap=self.laptop     #assign inner class to outer class

    class laptop:
        def __init__(self):
            self.brand='hp'
            self.cpu='i5'
            self.ram=8



s1=student('samim',1)   #crete object of student class

print(s1.name)

print(s1.lap)


#create object of laptop class
lap1=student.laptop

print(lap1.brand)





