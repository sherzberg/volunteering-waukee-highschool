Python Syntax > Functions
==========================

Functions
---------

```python

def print_hello():
    print("hello")

print_hello()

def add(x, y):
    return x + y

answer = add(1, 2)
print(answer)

a = 0
def calculate():
    a = 99
    print(a)
    
calculate()
print(a)

addition = add
print(addition(3, 4))

undeclared()
```

Keyword Arguments

```python
import random

def random_list(size=10):
    lst = []
    for i in range(size):
        lst.append(random.randrange(1, 101))
    return random_list

print(random_list())
print(random_list(2))
```

[Python Syntax](readme.md)

[Outline](../outline.md)
