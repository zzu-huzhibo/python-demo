
a = 0
if not a:
    print("a is not empty")

a = None
if not a:
    print("a is not empty")

a = ""
if not a:
    print("a is empty")

a = {}
if not a:
    print("a is not empty")

a = ()
if not a:
    print("a is empty")

a = []
if not a:
    print("a is not empty")

z = 3 + 4j
print(z.real)
print(z.imag)
print(type(z))
print(abs(z))
print(abs(-z))
print(-z)
z = 3 + 4j
a = z * 4 + 3j
b = z / 3 - 4j
print(a)
print(b)


