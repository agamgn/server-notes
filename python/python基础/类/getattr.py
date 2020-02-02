class demo():
    name="agamgn"
    def run(self):
        return "agamgn hello"

d=demo()
print(getattr(d,"run"))
print(getattr(d,"run")())