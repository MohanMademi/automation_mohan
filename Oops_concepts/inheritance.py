
# INHERITANCE:




# SINGLE LEVEL INHERITANCE:
class Parent:
    def fun1 (self):
        print('this is parent')

class Child(Parent):
    def fun2 (self):
        print("this is chaild")

Obj = Child()
Obj.fun2()
Obj.fun1()
print("---------------------------------------------")


# MULTI LEVEL INHERITANCE:
class Grandparent:
    def fun1 (self):
        print("grand parent function")
class Parent(Grandparent):
    def fun2(self):
        print("parant function")
class Child(Parent):
    def fun3(self):
        print("chaild function")

obj = Child()
obj.fun1()
# obj.fun2()
obj.fun3()
print("------------------------------------------------")




# INHIRICAL INHERTANCE:

class Parent:
    def fun1(self):
        print("this is parent")

class Child1(Parent):
    def fun2(self):
        print("this is child1")

class Child2(Parent):
    def fun3(self):
        print("this is child3")

obj=Child1()
# obj=Child2()

obj.fun1()
obj.fun2()
# obj.fun3()
print("-------------------------------------------------")



# MULTIPLE INHERITANCE:"


class Father:
    def fun1(self):
        print("this is father")

class Mother:
    def fun2(self):
        print("this is mother")

class Child(Father,Mother):
    def fun3(self):
        print("this is child")

obj=Child()
obj.fun3()
obj.fun1()
obj.fun2()
print("-------------------------------------------")











