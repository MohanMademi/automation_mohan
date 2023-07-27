
# CLASS AND OBJECT CREATION:


class Student:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age

    def fun1(self):
        print(self.id,self.age)
    def fun2(self):
        print(self.name,self.age)
        print("------------------------")

# WE CAN CREATE MULTIPLE OBJECTS IN A CLASS:
v1 = Student(1,"mohan",25)
v2 = Student(1,"mademi",24)
v1.fun1()
v1.fun2()
v2.fun1()
v2.fun2()


# CLASS 5 TIME WE NEED USING FOR METHOD:
class Student:
     def fun1(self):
        print("mohan")
     def fun2(self):
        print("mademi")
        print("---------------------")

# WE CAN CREATE FOR LOOP IN FOR NEED HOW MANY TIMES WE WANT:
for i in range(6):

    obj=Student()
    obj.fun1()
    obj.fun2()






















