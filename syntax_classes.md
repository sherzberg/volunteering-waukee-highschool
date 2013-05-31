Classes
============

Examples
--------------

```python
import math

class Ball(object):
    def __init__(self, radius):
        self.radius = radius
    def get_circumference(self):
        return 2 * self.radius * math.pi

ball = Ball(5)

print(ball.get_circumference())
```

[Outline](outline.md)
