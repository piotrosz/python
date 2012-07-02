#python classes

class MyClass:
    
    i = 2
    def f(self) :
        return 'hello world'

    def __init__(self):
        self.data = ['baba', 'baaba']


print(MyClass.i);
print(MyClass.f);

#instantiation

x = MyClass()

print(x.data)

print(x.f())


