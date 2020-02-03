import time

# 普通的类装饰器
class Foo:
    def __init__(self,func):
        self._func=func

    def __call__(self):
        print("class decorator start")
        self._func()
        print("class decorator end")

@Foo
def now():
    print(time.strftime("%Y-%m-%d",time.localtime(time.time())))

now()


# 带参数的类装饰器
class logger:
    def __init__(self,level='INFO'):
        self.level=level
    def __call__(self,func):
        def wrapper(*args,**kwargs):
            print("[{level}]:the function {func}() is run".format(
                level=self.level,func=func.__name__))
            func(*args,**kwargs)
        return wrapper
@logger(level="WARNING")
def say(something):
    print("say {}!".format(something))
say("hello")



# 修饰类的装饰器
def typed(**kwargs):
    def deco(obj):
        for k, v in kwargs.items():
            setattr(obj, k, v)
        return obj
    return deco

@typed(x=1, y=2, z=3)
class Foo:
    pass
print(Foo.__dict__)
@typed(name='alex')
class Bar:
    pass
print(Bar.__dict__)