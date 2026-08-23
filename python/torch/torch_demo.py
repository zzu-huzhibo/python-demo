import torch

A = torch.arange(1, 17).reshape(4, 4)

print(A)
print("访问张量中的元素=============================")
# 一个元素
print(A[1, 2])
# 第二行
print(A[1, :])
# 第二列
print(A[:, 1])
# 子区域 [1:3, 1:]
print(A[1:3, 1:])
# 子区域[::3, ::2]
print(A[::3, ::2])

print("正交矩阵,对称矩阵,满秩矩阵=============================")
B = torch.tensor([[1, 0, 0, 0], [0, 1, 0, 0, ], [0, 0, 1, 0], [0, 0, 0, 1]])
print(B)

print("张量的数学运算=============================")
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)

print("张量连接")
x = torch.arange(12, dtype=torch.float32).reshape(3, 4)
y = torch.tensor([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print("dim=0， 行合并")
print(torch.cat((x, y), dim=0))
print("dim=1， 列合并")
print(torch.cat((x, y), dim=1))

print("按照元素比较")
print(x == y)

print("按元素求和")
print(x.sum())

print("广播机制")
a = torch.arange(3).reshape((3, 1))
b = torch.arange(2).reshape((1, 2))
print(a)
print(b)
print(a + b)

x = torch.arange(12).reshape((3, 4))
print(x[-1])
print(x[1:3])
x[1, 3] = 9
print(x)
x[0:2, :] = 12
print(x)

print("分配内存")
print("执行加法运算后会重新分匹配内存给y")
before = id(x)
y = y + x
print(id(y) == before)
print("可以使用原地操作")
Z = torch.zeros_like(y)
print('id(Z):', id(Z))
Z[:] = x + y
print('id(Z):', id(Z))

print("如果后续运算中没有使用x，也可以赋值给x")
before = id(x)
x += y
print(id(x) == before)

print("转换为其他Python对象")
A = x.numpy()
B = torch.tensor(A)
print(type(A))
print(type(B))


print(torch.cuda.is_available())  # True
print(torch.cuda.get_device_name(0))  # NVIDIA GeForce RTX 4060 Ti
print(torch.version.cuda)  # PyTorch 编译时的 CUDA 版本
