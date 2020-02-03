var=99
def func():
    def innerfunc():
        global var
        print("var=",var)
        var =100
    return innerfunc
func()()
print(var)
# var= 99
# 100