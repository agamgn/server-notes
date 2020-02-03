# demo1
def func1():
    vars1=300
    print(vars1)

vars1=100
func1()
print(vars1)


# demo2
def func2():
    var2=100
    print(var2)
    def innerfunc2():
        print(var2)
    innerfunc2()
var2=200
func2()
print(var2)


# demo3
var3=300
def func3():
    var3=200
func3()
print(var3)