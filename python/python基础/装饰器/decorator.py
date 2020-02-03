# 函数作为返回值
def foo(num):
    return num+1
def bar():
    return foo
print(bar()(2))

# 函数作为参数
def foo(num):
    return num+1
def bar(func):
    return func(2)
print(bar(foo))


# 嵌套函数
def outer():
    x=1
    def inner():
        print(x)
    inner()
outer()

# 闭包
def outer():
    x=1
    def inner():
        print(x)
    return inner
print(outer()())


# 普通装饰器
def foo():
    print("foo")

def outer(func):
    def inner():
        print("logging start")
        func()
        print("logging end")
    return inner

foo=outer(foo)
foo()
# logging start
# foo
# logging end

# @
@outer
def foo():
    print("foo2")
foo()


def log(func):
    def inner(*args,**kw):
        print("logging start")
        func(*args,**kw)
        print("logging end")
    return inner
@log
def foo(name):
    print("hello "+name)

foo("agamgn")


# 带参数的装饰器
def sayHello(hello):
    def wrapper(func):
        def inner(*args,**kw):
            print("logging start")
            print(hello)
            func(*args,**kw)
            print("logging end")
        return inner
    return wrapper
@sayHello("hello")
def agam(name):
    print(name)
agam("agamgn")


# 多个装饰器
def outer1(func):
    def inner(*args,**kw):
        print("outer1 start")
        func(*args,**kw)
        print("outer1 end")
    return inner

def outer2(func):
    def inner(*args,**kw):
        print("outer2 start")
        func(*args,**kw)
        print("outer2 end")
    return inner
@outer1
@outer2
def foo():
    print("foo")
foo()