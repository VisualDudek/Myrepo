print("Hello world")

print('----------------')# Przykłady użycia lambda

y = lambda x: x**2
print(y(2))
print(type(y))

def h(n):
    return lambda x: x**n

a = h(2)
b = h(3)
print(a(2),' ',b(2))
