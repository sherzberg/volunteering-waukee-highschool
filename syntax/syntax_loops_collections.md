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
while current < sentinal:
    print(current)
    current += 1
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

[Python Syntax](syntax.md)
[Outline](outline.md)
