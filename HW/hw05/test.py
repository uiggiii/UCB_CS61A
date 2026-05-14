'''

def gene(x):
    for i in range(5):
        yield x + i

t = gene(3)
while True:
    input()
    print(next(t))

    '''

'''
g = (i for i in range(4))
print(next(g))
g.send(999)
print(next(g))

def h():
    yield 0
    x = yield 999
    yield 1

f = h()
print(next(f))
print(f.send(999))
print(next(f))



def g():
    y = yield 3
    print(y)
    print(666)
    yield 4
h = g()
print(next(h))
h.send(999)


def gen():
    x = yield 1      # ① 执行到这里会暂停，返回1
    print(f"收到: {x}")
    yield 2      # ② 继续执行时，send的值会赋给x
    
g = gen()
print(next(g))       # 输出 1，执行到 ① 处暂停
print(g.send(100))   # 输出 "收到: 100"，然后 ② 处返回2
'''
''''
class tree:
    def __init__(self, label, branch=[]):
        self.label = label
        self.branch = branch
        self = [label] + branch
    
    def is_tree(self):
        if type(self) == list and len(self) >= 1:
            return True
        else:
            return False
    
t = tree(3)
print(t.is_tree())
print(t)

'''
def yield_paths(t, value):
    """
    Yields all possible paths from the root of t to a node with the label
    value as a list.

    >>> t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
    >>> print_tree(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(yield_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = yield_paths(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = tree(0, [tree(2, [t1])])
    >>> print_tree(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = yield_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    if label(t) == value:
        yield t
    for b in branches(t):
        for g in yield_paths(b, value):
            yield [label(t)] + g

t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
t2 = tree(0, [tree(2, [t1])])
print(list(yield_paths(t2, 2)))