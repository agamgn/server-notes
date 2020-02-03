class A:
    def __new__(cls):
        return "abc"
class B:
    pass

print(A())
print(B())



# 用法
