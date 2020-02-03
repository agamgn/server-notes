class A:
    def __init__(self,name):
        self.name=name

a=A("agamgn")
print(a.name)

class B:
    def __new__(cls):
        print("__new__方法被执行")

    def __init__(self):
        print("__init__方法被执行")
b=B()


class C:
    def __new__(cls):
        print("__new__方法被执行")
        return super(C,cls).__new__(cls)
    def __init__(self):
        print("__init__方法被执行")

c=C()
