# better algorithm

我想在笔记最前端展示一些我在课上学到的优雅而通用的算法，它们来自homework，lab,discussion,projects,or me.
### 一种不需要for，if就可以重复循环的例子
```python
index = len(list) - 1
def f():
    nonlocal index
    index = (index + 1) % len(list)
    return list[index]
```

### 两个可以让函数随时变化的例子（闭包，类）
```python
# 闭包
def make_counter():
    count = 0

    def f():
        nonlocal count
        count += 1
        print(count)

    return f


```




<p>&nbsp;</p>
<p>&nbsp;</p>

# High order function
## 嵌套函数
```python
def adder(n):
    def add(k):     #def一个f(x)返回f，可以逐次接受参量
        return k + n
    return add
```
## 独立函数
```python
def f(x, y):
    return g(x)
    def g(x):
        return f(x, y)
result = f(1, 2)

'''
>>> can not find y
'''
```
独立函数中，各函数无法跨帧索引变量，因此难以实现变量的梦幻协同。

还有一些例子供学习绘制环境帧图使用。
```python
x = 12
def f():
    x = 10
    def g(y):
        return y + 2
    return g

rub = f()(3)
print(x)
```
<p>&nbsp;</p>
<p>&nbsp;</p>

# lambda expression
```python
identity(x) = lambda x : x
square(x) = lambda x: x *x
add(x, y) = lambda x, y: x + y
```
同样的，lambda expression 可以直接作为函数使用
```python
(lambda x: x * x)(3)

'''
>>> 9
'''
```
<p>&nbsp;</p>
<p>&nbsp;</p>

# Curry function

**函数柯里化**
当函数的几个变量时而固定，时而变化，需要灵活取用时，函数curry化是一个不错的选择。
```python
def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g
```
举个例子，
```python
from os import add

def do_func2(f):
    def adder(x):
        def add(y):
            return f(x, y)
        return add
    return adder

make_adder = do_func2(add)
make_addthree = make_adder(3)

make_addthree(2)

'''
>>> 5
'''
```
对curry化的函数输入args可以产生**偏函数**（or say **延迟函数**），可以让我们不用重复编写一个功能或者对函数某一个参量进行反复的修改。

另一种使用lambda expression的优雅表达方式如下：
```python
curry2 = lambda f: lambda x: lambda y: f(x, y)
```
<p>&nbsp;</p>
<p>&nbsp;</p>

# Decorator
Decorator 属于一种语法糖，它使用@加在一段代码前，起到高阶函数作用。和for，int等函数一样，让代码变得更加简洁易懂。
```python
def decorator(f):
    def wrapper(x):
        print('before function excuted')
        f()
        print('after function excuted')
    return wrapper

@decorator
def f():
    print('hello!')
``` 
<p>&nbsp;</p>
<p>&nbsp;</p>

# Recurison

递归函数的基本框架如下
```python
def f(*args, **kyargs):
    base case       # like if x == 0:return x

    recursive case      #like return x + f(x - 1)
```
举个例子，
```python
def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)
```
可以用它来生成重函数：
```python
def make_repeater(f, n):
    def g(x):
        if n == 1:
            return f(x)
        return f(make_repeater(f, n-1))
    return g
```
一个好的建议是，由于递归函数本身有些难以理解，因此最好将一些逻辑表达式def成函数。


## leap of faith
 阅读一个递归函数的一般流程(you'd better to believe in your code)：
 
    1.检测base case是否正确输出并且终止递归过程
 
    2.假设并相信你的f(x - 1)输出正确的结果

    3.观察你的f(x)是否能返回正确的结果

    4.if can,take your leap of faith to excute your code !


这是一个特别的chapter，我第一次在完成一份代码作业后如此兴奋，尽管我花了很久时间可能是一个占比很大的原因。anyhow，这是一个里程碑式的纪念。

题目是CS61A recursion discussion 第一题，要求使用**递归**方法将一个数**回文**输出。

这是代码的提示部分：
```python
def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
```

答案如下：

```python
def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else: 
        print(n % 10)
        def bounce(x):
            print(n % 10)
        bounce(swipe(n // 10))
```
我顿悟了，我像阿基米德一样跑了一圈又回来，我被震撼了
<p>&nbsp;</p>

同样是discussion的题，要求机器人最终停留在这一行的中点，限制是不能使用if,while,不能定义函数，不能赋值。只能call `main`, `front_is_clear()`, `front_is_blocked()`, `turn_left()`, `move()` 我想了一个多小时也没想出来，以下是Gemini给的代码：
```python
def main():
    if front_is_clear():
        move()
        if front_is_clear():        #防止连续走两步撞墙
            move()
            main()          #一个截断点，在这之前为递，之后为归
            turn_left()
            turn_left()
            move()
            turn_left()
            turn_left()
```
思路是向前走每次走两步，然后在回收帧过程中执行剩余的代码，每次挪动一步。amazing！

### 奇偶交替
```python
def digit_distance(n):
    """Determines the digit distance of n.

    >>> digit_distance(3)
    0
    >>> digit_distance(777) # 0 + 0
    0
    >>> digit_distance(314) # 2 + 3
    5
    >>> digit_distance(31415926535) # 2 + 3 + 3 + 4 + ... + 2
    32
    >>> digit_distance(3464660003)  # 1 + 2 + 2 + 2 + ... + 3
    16
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(HW_SOURCE_FILE, 'digit_distance',
    ...       ['For', 'While'])
    True
    """
```
solution很简洁，我也考虑了这种方法，但是我想到无法判定 k == n 时的奇偶性就放弃了，没想到如果从 1 开始的话 k 必定是奇数
```python
def sum_from(k):
        if k > n:
            return 0
        elif k == n:
            return odd_func(k)
        else:
            return odd_func(k) + even_func(k+1) + sum_from(k + 2)
    return sum_from(1)
```

我的答案如下
```python
   def helper_1(k):
        if k == n:
            return odd_func(k)
        if k == n-1:
            return odd_func(k) + helper_2(k+1)
        return helper_2(k+1) + odd_func(k)
    
    def helper_2(k):
        if k == n:
            return even_func(k)
        if k == n-1:
            return even_func(k) + helper_1(k+1)
        return helper_1(k+1) + even_func(k)
    
    return helper_1(1)
```
为了达到奇偶交替，这里使用两个函数相互call，base case还要分类多种情况，相比之下，类似思路由Claude给出的代码就好得多。它利用一个奇偶开关达到了交替的效果。
```python
def interleaved_sum(n, odd_func, even_func):
    def helper(k, use_odd):
        if k > n:
            return 0
        if use_odd:
            return odd_func(k) + helper(k+1, False)
        else:
            return even_func(k) + helper(k+1, True)
    return helper(1, True)
```

## tree recursion
### num partitions
给定一个数字 n ，以小于 m 的数字进行partition

     思路：(6, 4) -> (6, 3) + (2, 4)   #不包含4/包含4
```python
def patitions(n, m):
    if n == 0:
        return 1
    if n < 0:
        return 0
    else:
        with_m = patitions(n-m, m)
        without_m = patitions(n, m-1)
    return with_m + without_m
```
### make changes
```python
def next_smaller_dollar(bill):
    """Returns the next smaller bill in order."""
    if bill == 100:
        return 50
    if bill == 50:
        return 20
    if bill == 20:
        return 10
    elif bill == 10:
        return 5
    elif bill == 5:
        return 1


def count_dollars(total):
    """Return the number of ways to make change.

    >>> count_dollars(15)  # 15 $1 bills, 10 $1 & 1 $5 bills, ... 1 $5 & 1 $10 bills
    6
    >>> count_dollars(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills
    4
    >>> count_dollars(20)  # 20 $1 bills, 15 $1 & $5 bills, ... 1 $20 bill
    10
    >>> count_dollars(45)  # How many ways to make change for 45 dollars?
    44
    >>> count_dollars(100) # How many ways to make change for 100 dollars?
    344
    >>> count_dollars(200) # How many ways to make change for 200 dollars?
    3274
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_dollars', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    assert total >= 0, "n can't be negative."
    def count(n, bill):
        if n == 0:
            return 1
        if n < 0:
            return 0
        if bill == 1:
            return 1
        else:
            a = count(n-bill, bill)
            b = count(n, next_smaller_dollar(bill))
            return a + b
    return count(total, 100)
```

<p>&nbsp;</p>

### lambda caculus
如果函数均为匿名函数(lambda 表达式)，如何用其构建基础的语法，true，false，if，还有高阶方法如递归等？

`λx.λy.x`  True

`λx.λy.y`  False

`λb.(λx.λy.b(xy))`  if then

`λb.(λx.λy.(b(λx.λy.x)(λx.λy.y)))` not

`λa.λb.(a(b)(λx.λy.y))` and

`λa.λb.(a(λx.λy.x)(b))` or

`λf.(λx.f(xx))(λx.f(xx))` Y组合子，可以用于无限递归

`λf.(λx.f(xxv))(λx.f(xxv))` Z组合子，严格求值，用于实际编程语言中递归

以python语言为例，分析Y组合子
```python
Y = lambda f:(lambda x:f(x(x))(lambda x:f(x(x))))

lambda f    
'''
类似于一个循环的启动子，接受后来的lambda x,并将lambda x:f(x(x))作用于lambda x:f(x(x)),每次作用，一个f(x(x))可以产生两个itself，从而实现递推延伸。
'''
lambda x:f(x(x))    # 循环套件

```
```python
def g(fuc):         # 启动子λf
    return fuc(fuc)

# 利用z组合子计算n的factorials
def u(f):
    def time(n):
        if n == 0:
            return 1
        else:
            return n *f(f(n-1))
    return time
```
<p>&nbsp;</p>
<p>&nbsp;</p>

# sequence

list可以更改，但是不能用一个新的变量引用来对list中的元素进行更改

```python
list = [1, 2, 3]
for i in list:
    i += 1

list
>>>[1, 2, 3]        # i += 1的操作实际创造了新的对象并且将i的引用更改至该内存地址，而非实际更改了list



```python
# list 乘法是对整体repeat， 而不是对元素
list = [1, 2, 3]
list * 2 == [1, 2, 3, 1, 2, 3]


# list 中的列表也可读取
list == [[1, 2], [2, 2]]
for x, y in list:
    xxx


# 当不需要索引值时
for _ in range(1, 4):
    xxx


# sum,max,min  函数
# 接受一个可迭代对象，可以按照key_func计算后返回 
sum(iterable, key_func= )       
max(iterable, key_func= )
min(iterable, key_func= )

lst.reverse()       # 直接对对象反向，返回none


```

```python
# 四舍六入五取偶
round(num, k)

'''
round(3.1)
>>> 3

round(3.1415, 3)
>>> 3.142

# 缓冲代码pass
if True:
    pass
else:
    f(x)

# 函数特性
func.__name__  
>>> func
'''

# all函数，接收一个iterable, 只有在全为真时返回True
# any函数，接收一个iterable，存在一真则为True
all([1, 2, 0])
any([1, 2, 0])
>>> False
>>> True

```

<p>&nbsp;</p>
<p>&nbsp;</p>

# dictionary

键值对的集合
```python
dic = {1:'hello', 2:'world'}

list(dic)
dic.value()

>>> [1, 2]
>>> {['hello', 'world']}

# 创建字典
def index(keys, values, match):
    return {k:[v for v in values if match(k, v)] for k in keys}

index([1, 2, 3, 4], range(20), lambda x, y:y == x*x)

>>> {1: [1], 2: [4], 3: [9], 4: [16]}

# 创建一个含有多个空列表的列表
[[] for _ in range(n)]
[<map expression> for <name> in <sequence expression> if <filter expression>]
```

<p>&nbsp;</p>
<p>&nbsp;</p>

# tree
```python
# sum函数的应用
'''sum函数本质是加法，因此当给予一个空列表时，sum可以输出一个列表'''
sum([[1, 2, 3]], [[4, 5]] [])


>>> [1, 2, 3, 4, 5]


# tree structure

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

raise AssertionError('fuk')

```

<p>&nbsp;</p>
<p>&nbsp;</p>


# mutability

函数默认参数值最好避免使用可变参数值，比如s=[]，以防每次调用函数时该参数都会发生变化
```python
def print_len(s=[])
    s.append(3)
    print(len(s))

print_len()
print_len()
print_len()

>>> 1
>>> 2
>>> 3
```

<p>&nbsp;</p>
<p>&nbsp;</p>

# iterators
函数iter记录下一个迭代对象的位置，next则**先返回**iter记录的位置对应的值，然后再向前移动
```python
list = [1, 2, 3, 4]
i = iter(list)      #生成迭代器
print(i)

>>> 0xdh435ffdg5321

# 移动指针
print(next(i))

>>> 1

# for 不仅可以用于iterable object，还可以用于iterator
it = iter(list)
for i in it:        #for 会自动next()
    print(i)

>>> 1
>>> 2
>>> 3
>>> 4
# 此时it已经迭代到end
for i in it:
    print(i)

# nothing
```

有些object为惰性计算，只有在调用时才计算出目标值然后next，并且不存储数据，这意味着当你需要调用某个指定项时，
它需要迭代到目标位置才能输出结果，用时间换空间

比如map，range，reserved，其中range由于通用性强，其使用公式来计算目标值，因而可以直接调用任一项


<p>&nbsp;</p>

## zip
zip函数可以将多个iterable objects 相同index的element以tuple存储,len取最小值
```python 
zip([1, 2], [2, 4, 5], [6, 7])

>>> [(1, 2, 6), (2, 4, 7)]
```

<p>&nbsp;</p>
<p>&nbsp;</p>

# generator
generator是由yield自动生成的特殊iterator，无需维护

```python
g = (i for i in range(4))

def g(x):
    yield x
    yield -x
```

generator 的一些方法
send方法会向**停留处的yield**传入value，next等价于send（None），因为yield是一种双向通道，不仅会输出还能输入
```python
def g():
    x = yield 2
    y = yield 3
    print(y)

h = g()
print(next(h))
print(h.send(999))

>>> 2
>>> 3
>>> 999
```
`g.close()`终止generator
`yield form` 允许generator从其他iterator拉取value





# object
变量不会指向变量，如果一个变量指向另一个变量，它不会在此停留，而是继续下去，直到指向一个object为止

```python
a = 1       # 对象复用
b = 1
a is b

>>> True

a = []
b = []
a is b

>>> False
```

<p>&nbsp;</p>
<p>&nbsp;</p>


# class
class 在我的理解中是定义出一套完备的，逻辑自洽的系统，类似于数学中开辟复数域，附带一整套可以作用于该系统的方法。

class 中的__init__默认返回none,不能return

为了复用父类逻辑，在子类中通过 super() 按继承链顺序调用父类方法


class中的函数本质也是attribute，也可以进行更改，注意传入参数依旧是self而不是临时状态
```python
class A:
    def f(self):
        print(1)

A.f = lambda self:print(2)

a = A()
a.f()

>>> 2
```

## Attribute
除class外，函数对象也有属性