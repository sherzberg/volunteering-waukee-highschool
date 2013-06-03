Python Syntax > Loops & Iterables
====================================

Strings
--------

```python
my_string = "abcdefg"

print(len(my_string))
for ch in my_string:
    print ch
```

Lists
--------

```python
print([0,1,2,3,4,5,6,7,8,9])
print(range(10))
print(len(range(10)))

for x in range(1, 10, 2):
    print(x)

sentinel = 4
current = 0
while current < sentinel:
    print(current)
    current += 1

l = [1,2,3]
l.append(4)
print(l)

print(l[0])
l[0] = 4
print(l)
```

Sets
--------

```python
print({1,2,3,3})
print(set([1,2,3,3]))

s = {1,2,2}
s.add(2)
print(s)
```

Tuples
-------

```python
a = (1, 2, 2,)
print(a)
```

Dictionaries
------------

```python
d = {}
d['key'] = 123
d['otherkey'] = "hello"
print(d)

for key in d:
    print(key)
    print(d[key])
    print('-------')

for key, value in d.items():
    print(key + ", " + str(value))

print("string" in d)
print("key" in d)

```

[Python Syntax](readme.md)

[Outline](../outline.md)
