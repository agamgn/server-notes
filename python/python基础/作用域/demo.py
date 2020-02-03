# 局部作用域
def func():
    x=1
    print(x)

#print(x)# name 'x' is not defined


# 嵌套作用域
def func():
    x=1
    def innerfunc():
        print(x)
    innerfunc()
func()

# 全局作用域
funcnum=10
def func():
    print (funcnum)
func()


