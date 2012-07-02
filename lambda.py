def linear(a=1, b=0):
    return lambda x: a*x + b

f = linear()
print(f(0))
print(f(1))
print(f(10))

f2 = linear(2, 3)
print(f2(0))
print(f2(10))
