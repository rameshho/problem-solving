class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            print("ramesh")
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self, arg):
        print("Hosamani")
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg
    def __str__(self):
        print("outer")
        return OnlyOne.instance.val
    def __getattr__(self, name):
        return getattr(self.instance, name)

x = OnlyOne('sausage')
print(x)
y = OnlyOne('eggs')
print(y)
z = OnlyOne('spam')
print("------------------")
print(z)
print(x)
print(y)
