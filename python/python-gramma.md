# Python 语法总结

---

## 1. 概述

Python 是一门优雅而健壮的编程语言，由荷兰人 Guido van Rossum 于 1989 年开始编写。设计哲学是「优雅」「明确」「简单」。Python 是解释型语言，代码在执行时逐行翻译为机器码。

- Python 3.x 是当前和未来主流版本
- Python 是动态类型语言，变量不需要声明类型
- Python 支持面向过程和面向对象两种编程范式

---

## 2. 基础语法

### 2.1 注释

```python
# 单行注释

"""
多行注释（实际上是多行字符串）
也可以用三个单引号
"""
```

### 2.2 变量

- 变量不需要声明，赋值后自动创建
- Python 中一切都是对象，变量本质上是对象的引用

```python
name = "张三"
age = 18
weight = 1000.3
var1 = var2 = var3 = 10  # 多变量同值
a, b, c = 10, 20, 30     # 多变量不同值
```

### 2.3 标识符命名规则

- 只能包含字母、数字和下划线，不能以数字开头
- 区分大小写
- 不能与关键字重复
- 应既简短又具有描述性

**命名方法：**

- 大驼峰：`UpperCamelCase`（类名常用）
- 小驼峰：`lowerCamelCase`
- 蛇形命名：`snake_case`（Python 推荐，变量名/函数名常用）

### 2.4 常量

Python 中没有内置常量类型，约定使用全大写变量名表示：

```python
PI = 3.1415926
E = 2.718282
```

---

## 3. 数据类型

### 3.1 基本数据类型

| 类型 | 说明 | 示例 |
|------|------|------|
| `int` | 整数（任意大小） | `10`, `-5`, `1_000_000` |
| `float` | 浮点数 | `3.14`, `1.3e7` |
| `bool` | 布尔值（int子类） | `True`, `False` |
| `complex` | 复数 | `3+4j` |
| `str` | 字符串（不可变） | `"hello"`, `'world'` |

**注意：** `True == 1`, `False == 0`，但 `True is 1` 为 `False`。

能够解释为假的值：`None`, `0`, `0.0`, `False`, 空容器（空列表、空元组、空字典、空集合、空字符串）

### 3.2 容器数据类型

| 类型 | 说明 | 可变性 | 有序性 |
|------|------|--------|--------|
| `list` | 列表 | 可变 | 有序 |
| `tuple` | 元组 | 不可变 | 有序 |
| `set` | 集合 | 可变 | 无序 |
| `dict` | 字典 | 可变 | 有序(3.7+) |

**不可变类型：** `int`, `float`, `bool`, `str`, `tuple`
**可变类型：** `list`, `set`, `dict`

### 3.3 类型判断与转换

```python
type(x)             # 返回精确类型
isinstance(x, int)  # 判断类型（考虑继承关系，bool是int子类）

int("123")      # 字符串转整数
float("3.14")   # 字符串转浮点数
str(100)        # 数字转字符串
list("abc")     # 转为列表 ['a', 'b', 'c']
tuple([1,2])    # 转为元组 (1, 2)
set([1,2,2])    # 转为集合 {1, 2}
```

### 3.4 编码与解码

```python
s = "你好中国"
b = s.encode('utf-8')   # 编码：字符串 -> bytes
s2 = b.decode('utf-8')  # 解码：bytes -> 字符串
```

---

## 4. 输入与输出

### 4.1 输入

```python
name = input("请输入姓名：")       # 返回字符串类型
age = int(input("请输入年龄："))    # 转换类型
```

### 4.2 输出与格式化

```python
print("Hello Python")
print("Hello", "World")
print("结果:", end="")              # 控制结尾字符

# f-string（推荐）
print(f"name={name}, age={age}")
print(f"{3.14159:.2f}")             # 保留两位小数
print(f"{1000000:,}")               # 千位分隔
print(f"{0.256:.1%}")               # 百分比
print(f"{value = }")                # 自动输出 变量名=value

# format 方法
print("name={}, age={}".format(name, age))

# % 占位符
print("name=%s, age=%d" % (name, age))
```

---

## 5. 运算符

### 5.1 算术运算符

| 运算符 | 说明 | 示例 |
|--------|------|------|
| `+` | 加 | `3 + 2 = 5` |
| `-` | 减 | `3 - 2 = 1` |
| `*` | 乘 | `3 * 2 = 6` |
| `/` | 除（结果为浮点数） | `7 / 2 = 3.5` |
| `//` | 整除（向下取整） | `7 // 2 = 3` |
| `%` | 取余 | `7 % 2 = 1` |
| `**` | 幂运算 | `2 ** 3 = 8` |

### 5.2 比较运算符

`==`, `!=`, `>`, `<`, `>=`, `<=`

### 5.3 逻辑运算符

`and`, `or`, `not`

```python
print(5 and 8)   # 8（返回最后一个真值）
print(0 and 8)   # 0
print(5 or 8)    # 5（返回第一个真值）
print(0 or 8)    # 8
print(not(5))    # False
```

### 5.4 赋值运算符

`=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`

### 5.5 位运算符

`&`(与), `|`(或), `^`(异或), `~`(按位取反), `<<`(左移), `>>`(右移)

位运算以补码形式进行计算。

### 5.6 成员运算符与身份运算符

```python
# 成员运算符
1 in [1, 2, 3]       # True

# 身份运算符（比较内存地址）
a = [1, 2, 3]
b = a                 # b is a -> True
b = a[:]              # b is a -> False, b == a -> True
```

### 5.7 运算符优先级

从高到低：`**` > `~` `+` `-` > `*` `/` `//` `%` > `+` `-` > `>>` `<<` > `&` > `^` > `|` > `>` `>=` `<` `<=` `==` `!=` > `not` > `and` > `or`

---

## 6. 流程控制

### 6.1 条件语句

```python
# 单分支
if 条件:
    语句块

# 双分支
if 条件:
    语句块1
else:
    语句块2

# 多分支
if 条件1:
    语句块1
elif 条件2:
    语句块2
else:
    语句块3

# match-case（Python 3.10+）
match value:
    case 模式1:
        语句1
    case 模式2:
        语句2
    case _:
        默认语句
```

### 6.2 三目运算符

```python
max_num = a if a > b else b
```

### 6.3 循环语句

```python
# while 循环
while 条件:
    循环体

# while-else（循环正常结束时执行else）
while 条件:
    循环体
else:
    语句

# for 循环
for 临时变量 in 可迭代对象:
    循环体

# for-else
for 临时变量 in 可迭代对象:
    循环体
else:
    语句
```

### 6.4 range() 函数

```python
range(stop)              # 0 到 stop-1
range(start, stop)       # start 到 stop-1
range(start, stop, step) # 指定步长
```

### 6.5 循环控制

- `break`：跳出当前循环（循环的else不执行）
- `continue`：跳过本次循环，继续下一轮
- `pass`：空语句，保持程序结构完整

---

## 7. 容器数据类型

### 7.1 序列（Sequence）

列表、元组、字符串都是序列，支持以下通用操作：

- 索引：`sequence[0]`（从0开始，支持负索引）
- 切片：`sequence[1:3]`（左闭右开）
- 相加：`sequence1 + sequence2`
- 乘法：`sequence * 3`
- 检查成员：`x in sequence`
- 长度：`len(sequence)`
- 最大/最小值：`max(sequence)`, `min(sequence)`

### 7.2 列表 List

```python
# 创建
list1 = [100, 200, 300, 400, 500]

# 访问与切片
list1[0]       # 索引访问 -> 100
list1[-1]      # 倒数第一个 -> 500
list1[1:3]     # 切片 -> [200, 300]
list1[::-1]    # 倒序

# 添加元素
list1.append(600)       # 末尾追加
list1.insert(2, 700)    # 指定位置插入

# 修改
list1[0] = -1
list1[2:4] = ["a", "b", "c"]

# 删除
del list1[2]

# 遍历
for item in list1:
    print(item)
for i, val in enumerate(list1):
    print(i, val)

# 列表推导式
squares = [x**2 for x in range(10)]
squares = [x**2 for x in range(10) if x % 2 == 0]

# 常用函数
max(list1), min(list1), sum(list1), len(list1)
list1.copy()   # 浅拷贝
```

### 7.3 元组 Tuple

```python
# 创建
tuple1 = (100, 200, 300)
tuple1 = (100,)           # 单元素元组必须加逗号

# 元组不可修改元素，但可以重新赋值
# 元组中若包含可变类型（如列表），其内容可修改
t = (1, 2, [3, 4])
t[2].append(5)  # 合法，t变为 (1, 2, [3, 4, 5])
```

### 7.4 集合 Set

```python
# 创建
set1 = {1, 2, 3}
set2 = set([1, 2, 3])
set3 = set()            # 空集合（不能用{}，那是空字典）

# 添加/删除
set1.add(4)
set1.update([5, 6])
set1.remove(2)          # 删除（不存在报错）
set1.discard(10)        # 删除（不存在不报错）

# 集合运算
a | b   # 并集
a & b   # 交集
a - b   # 差集
a ^ b   # 对称差集
```

### 7.5 字典 Dictionary

```python
# 创建
dict1 = {"name": "Alice", "age": 18, "gender": "male"}
dict2 = dict(name="Bob", age=20)
dict3 = dict([("name", "Tom"), ("age", 22)])

# 访问
dict1["name"]              # 键访问（不存在报错）
dict1.get("name")          # get 方法（不存在返回 None）
dict1.get("addr", "未知")  # 指定默认值

# 添加/修改
dict1["address"] = "earth"
dict1["name"] = "Bob"

# 删除
del dict1["name"]

# 遍历
for key in dict1:
    print(key, dict1[key])
for key, value in dict1.items():
    print(key, value)

# 字典推导式
squares = {x: x**2 for x in range(4)}
```

---

## 8. 函数

### 8.1 函数定义

```python
def 函数名(参数列表):
    """文档字符串"""
    函数体
    return 返回值
```

### 8.2 参数类型

```python
# 必须参数（位置参数）
def func(a, b):
    return a + b

# 默认值参数（非默认参数必须在默认参数之前）
def func(name, age=20):
    print(name, age)

# 关键字参数（调用时指定参数名）
func(name="张三", age=18)

# 不定长参数
def func(*args):       # *args 接收多余位置参数，打包为元组
    print(args)
def func(**kwargs):    # **kwargs 接收多余关键字参数，打包为字典
    print(kwargs)

# 强制位置参数/关键字参数（Python 3.8+）
def f(a, b, /, c, d, *, e, f):
    # a, b 只能位置传参；e, f 只能关键字传参
    pass

# 解包传参
def func(a, b, c):
    return a + b + c
print(func(*[1, 2, 3]))                    # 列表/元组解包
print(func(**{"a": 1, "b": 2, "c": 3}))    # 字典解包
```

### 8.3 返回值

```python
def add(a, b):
    return a + b        # 返回一个值

def func():
    return 1, 2, 3      # 返回多个值（元组）

def func():
    pass                # 不返回或无return -> 返回 None
```

### 8.4 变量作用域（LEGB规则）

查找顺序：`Local`(局部) -> `Enclosing`(嵌套) -> `Global`(全局) -> `Built-in`(内置)

```python
a = int(2.9)  # 内建作用域
b = 0         # 全局作用域

def outer():
    c = 1     # 嵌套作用域
    def inner():
        d = 2 # 局部作用域
        print(d, c, b, a)
    return inner
```

### 8.5 global 与 nonlocal

```python
# global：在函数内修改全局变量
var1 = 100
def func():
    global var1
    var1 = 200

# nonlocal：在内部函数中修改外部函数的变量
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 100
    inner()
    print(x)  # 100
```

### 8.6 递归

```python
# 求阶乘
def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1
```

### 8.7 匿名函数 lambda

```python
lambda 参数列表: 表达式

# 示例
add = lambda x, y: x + y
print(add(1, 2))  # 3

# 常与内置函数搭配使用
students = [{"name": "zhang3", "age": 36}, {"name": "li4", "age": 14}]
print(sorted(students, key=lambda x: x["age"]))

# map() 对序列中元素逐一处理
list(map(lambda x: x * x, [0, 1, 3, 7, 9]))  # [0, 1, 9, 49, 81]

# filter() 对序列中元素过滤
list(filter(lambda x: x >= 0, [-1, 0, 3, 7]))  # [0, 3, 7]

# reduce() 对序列中元素进行累积
from functools import reduce
reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])  # 120
```

### 8.8 装饰器

```python
def decorator(func):
    def inner(*args, **kwargs):
        # 添加功能
        result = func(*args, **kwargs)
        # 添加功能
        return result
    return inner

@decorator
def say_hello():
    print("hello")
```

---

## 9. 面向对象

### 9.1 类和对象

- **类（Class）**：描述对象共同的属性和方法，是创建对象的模板
- **对象（Object）**：类的实例，是具体的

### 9.2 定义类

```python
class Person:
    """人的类"""

    home = "earth"          # 类属性

    def __init__(self, name):
        self.name = name    # 实例属性

    def eat(self):          # 实例方法
        print(f"{self.name} is eating...")

    @classmethod
    def come_from(cls):     # 类方法
        print(f"来自{cls.home}")

    @staticmethod
    def static_method():    # 静态方法
        print("static method")

# 实例化
p = Person("张三")
p.eat()
Person.come_from()
```

### 9.3 三大特性

**封装：** 将变量和函数写入类中，通过双下划线实现私有化

```python
class Person:
    def __init__(self, name):
        self.__name = name   # 私有属性

    @property
    def name(self):          # 只读属性
        return self.__name

    @name.setter
    def name(self, name):    # 读写属性
        self.__name = name
```

**继承：** 子类继承父类的属性和方法

```python
class Person:
    def eat(self):
        print("eating...")

class Chinese(Person):       # 单继承
    pass

class ChineseStudent(Student, YellowRace):  # 多继承
    pass

# 复用父类方法
super().eat()               # 推荐方式
Person.eat(self)            # 传统方式
```

**多态：** 同一方法在不同对象上呈现不同行为

```python
class Dog:
    def go(self):
        print("跑")

class Fish:
    def go(self):
        print("游")

def move(animal):
    animal.go()  # 不同对象执行不同方法
```

### 9.4 特殊方法（魔法方法）

```python
__init__()      # 初始化方法（构造函数）
__str__()       # 定义 str() 时的行为（人类可读）
__repr__()      # 定义 repr() 时的行为（机器可读）
__new__()       # 对象实例化时第一个调用
__del__()       # 对象销毁时调用
```

---

## 10. 文件操作

### 10.1 打开与关闭

```python
f = open("test.txt", "r", encoding="utf-8")
# ... 操作文件
f.close()

# 推荐使用 with 语句（自动关闭文件）
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

### 10.2 读写操作

```python
# 写
with open("test.txt", "w") as f:
    f.write("hello world\n")

# 读
with open("test.txt", "r") as f:
    f.read()       # 读取全部内容
    f.readline()   # 读取一行
    f.readlines()  # 读取所有行，返回列表
```

---

## 11. 异常处理

### 11.1 try-except

```python
try:
    result = 3 / 0
except ZeroDivisionError as e:
    print(e)
except (TypeError, NameError) as e:
    print(e)
except:
    print("Unexpected error")
else:
    print(f"结果是: {result}")    # 无异常时执行
finally:
    print("finally")              # 无论是否异常都执行
```

### 11.2 抛出异常

```python
# raise
raise TypeError("参数类型错误")

# assert 断言
assert isinstance(x, int), "参数类型错误"
```

### 11.3 with 语句

```python
with open("test.txt", "r") as f:
    content = f.read()
# 等价于 try-except-finally，自动调用 f.close()
```

---

## 12. 模块与包

### 12.1 模块导入

```python
import module_name              # 全部导入
import module_name as alias     # 导入并起别名
from module_name import func    # 局部导入
from module_name import *       # 导入所有公开成员
```

### 12.2 `__name__` 的作用

```python
if __name__ == "__main__":
    # 直接运行时执行，被导入时不执行
    main()
```

### 12.3 包

包是管理模块命名空间的方式，文件夹下必须有 `__init__.py` 文件。

```python
import graphic.circle          # 导入包中的模块
from graphic import circle     # 从包中导入模块
from graphic.circle import area # 从包中模块导入功能
```

### 12.4 安装第三方库

```bash
pip install 包名
pip install -i http://mirrors.aliyun.com/pypi/simple/ 包名  # 使用镜像源
pip list                    # 查看已安装的包
pip uninstall 包名           # 卸载
```

---

## 13. Python高级语法

### 13.1 浅拷贝与深拷贝

```python
import copy

# 浅拷贝：只拷贝第一层
list2 = copy.copy(list1)
list2 = list1[:]            # 切片拷贝
list2 = list(list1)         # 工厂函数

# 深拷贝：完全拷贝所有层
list3 = copy.deepcopy(list1)
```

### 13.2 迭代器

```python
# 可迭代对象：list, tuple, dict, set, str, generator
# 迭代器：实现了 __iter__() 和 __next__() 的对象

my_list = [1, 2, 3]
it = iter(my_list)           # 创建迭代器
print(next(it))              # 1
print(next(it))              # 2

for item in it:
    print(item)              # 3
```

### 13.3 生成器

```python
# 使用推导式创建
gen = (x for x in range(5))

# 使用 yield 创建
def fibo():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

f = fibo()
print(next(f))  # 1
print(next(f))  # 1
```

### 13.4 闭包

```python
def linear(a, b):
    def inner(x):
        return a * x + b
    return inner

y1 = linear(1, 1)
print(y1(5))  # 6
```

### 13.5 装饰器

```python
def decorator(func):
    def inner(*args, **kwargs):
        # 前置处理
        result = func(*args, **kwargs)
        # 后置处理
        return result
    return inner

@decorator
def my_func():
    print("hello")

# 带参数的装饰器
def times(n):
    def get_decorator(f):
        def inner(x):
            result = x
            for _ in range(n):
                result = f(result)
            return result
        return inner
    return get_decorator

@times(2)
def sqrt_val(x):
    from math import sqrt
    return sqrt(x)
```

---

## 14. 进程与线程

### 14.1 多进程

```python
import multiprocessing

def worker():
    print("Working")

if __name__ == "__main__":
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()

    # 进程池
    with multiprocessing.Pool(4) as pool:
        pool.map(worker, range(10))
```

### 14.2 多线程

```python
import threading

def worker():
    print(f"{threading.current_thread().name}: working")

t1 = threading.Thread(target=worker, name="Thread1")
t1.start()
t1.join()

# 互斥锁
lock = threading.Lock()
lock.acquire()
try:
    # 临界区代码
    pass
finally:
    lock.release()
```

### 14.3 GIL（全局解释器锁）

同一时间只允许一个线程保持 Python 解释器的控制权。CPU密集型任务建议使用多进程，IO密集型任务可以使用多线程。

---

## 15. 常用标准库

| 模块 | 说明 |
|------|------|
| `os` | 操作系统相关 |
| `sys` | 系统相关 |
| `math` | 数学运算 |
| `random` | 随机数 |
| `datetime` | 日期时间 |
| `json` | JSON处理 |
| `re` | 正则表达式 |
| `collections` | 高级容器类型 |
| `itertools` | 迭代器工具 |
| `functools` | 函数工具 |

---

