Importing Libraries
===================

Import
--------------

Importing libraries enables you to use others or your own code in
a reusable way.

For example, the Math library:

```python
import math

print(math.floor(123.31))

print(math.pi)

help(math)
```

Libraries
---------

There are tons of libraries built in:

* os
* sys
* zipfile
* time
* ... lots more

You can even import your own code. Create a file named library.py:

```python
# library.py

def multiply(x, y):
    return x * y
```

Create a main.py file (or start the intrepreter):

```python
import library

answer = library.multiply(5, 6)
print(answer)
```

[Python Syntax](readme.md)

[Outline](../outline.md)
