class demo():
    name="agamgn"
    def run(self):
        return "agamgn hello"

d=demo()
print(hasattr(d,"age"))#False
setattr(d,"age","18")
print(hasattr(d,"age"))#True