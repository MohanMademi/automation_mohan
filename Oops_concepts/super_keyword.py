class A:
    def __init__(self):
        print("this is a class")

    def fun1(self):
        print("this is A function")

class B(A):
    def __init__(self):
        print("this is b class")
        super().__init__()

    def fun2(self):
        print("this is B function")

obj=B()
obj.fun1()
obj.fun2()