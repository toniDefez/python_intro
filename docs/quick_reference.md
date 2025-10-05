# Python Quick Reference

This quick reference complements the Jupyter notebooks in this repository. Use it as a reminder of the core syntax and idioms you will encounter while working through the material.

## 1. Python Basics

### Running Python
```bash
python --version
python -m pip install --upgrade pip
python script.py
python -i script.py  # run and drop into REPL
```

### Variables and Types
```python
message = "Hello"
count = 10              # int
ratio = 3.14            # float
is_ready = True         # bool
nothing = None          # NoneType
```

Python is dynamically typed. Use `type(value)` to inspect a value's type.

### Strings
```python
name = "Ada"
len(name)            # 3
name.upper()         # 'ADA'
"-".join(["a", "b"])  # 'a-b'
"Value: {}".format(42)
f"Value: {42}"
```
Use triple quotes for multiline strings.

## 2. Numbers and Operators
```python
5 + 3    # addition
5 // 3   # floor division
5 % 3    # modulo
5 ** 2   # exponentiation
```
Comparison operators return booleans (`==`, `!=`, `<`, `<=`, `>`, `>=`). Combine expressions with `and`, `or`, and `not`.

## 3. Collections

### Lists
```python
items = [1, 2, 3]
items.append(4)
items[0]          # 1
items[-1]         # 4
items[1:3]        # [2, 3]
```

### Tuples
```python
point = (3, 4)
x, y = point
```

### Sets
```python
unique = {1, 2, 3}
unique.add(2)      # unchanged
unique | {3, 4}    # union: {1, 2, 3, 4}
```

### Dictionaries
```python
user = {"name": "Ada", "age": 37}
user["name"]          # 'Ada'
user.get("email", "")
for key, value in user.items():
    print(key, value)
```

### Comprehensions
```python
squares = [n**2 for n in range(5)]
odd_squares = {n: n**2 for n in range(5) if n % 2}
```

## 4. Control Flow
```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

for n in range(5):
    print(n)

while condition:
    do_something()

for index, value in enumerate(items):
    print(index, value)
```
Use `break`, `continue`, and `pass` when needed.

## 5. Functions
```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

result = greet("Ada")
```
Functions are first-class objects. You can pass them as arguments or return them from other functions.

### Lambda Functions
```python
add = lambda x, y: x + y
```
Use sparingly for simple one-line functions.

### Higher-Order Functions
```python
numbers = [1, 2, 3]
doubled = list(map(lambda n: n * 2, numbers))
even = list(filter(lambda n: n % 2 == 0, numbers))
from functools import reduce
product = reduce(lambda acc, n: acc * n, numbers, 1)
```

## 6. Modules and Packages
```python
import math
from pathlib import Path

import numpy as np
import pandas as pd
```
Use `if __name__ == "__main__":` to make scripts executable and importable.

### Virtual Environments
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 7. Object-Oriented Programming
```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "..."

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

pet: Animal = Dog("Luna")
pet.speak()  # 'Woof!'
```
Use properties to manage access and `@staticmethod`/`@classmethod` for alternative constructors.

## 8. Error Handling
```python
try:
    risky_operation()
except ValueError as exc:
    print(f"Invalid value: {exc}")
else:
    print("No exception raised")
finally:
    cleanup()
```
Raise exceptions with `raise ValueError("message")` when appropriate.

## 9. Files and Context Managers
```python
from pathlib import Path

path = Path("data.txt")
path.write_text("hello")
print(path.read_text())

with path.open("a", encoding="utf-8") as fh:
    fh.write("\nworld")
```

## 10. Testing and Quality
```bash
python -m unittest discover
pytest
ruff check .
```
Use type hints and `mypy` or `pyright` for static analysis.

## 11. Data Science Essentials

### NumPy
```python
import numpy as np

arr = np.array([1, 2, 3])
arr.mean()        # 2.0
arr.reshape(3, 1)
```

### pandas
```python
import pandas as pd

df = pd.DataFrame({"name": ["Ada", "Grace"], "age": [37, 36]})
df["age"].mean()
df[df["age"] > 36]
```

### Matplotlib
```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Example")
plt.show()
```

## 12. Next Steps

* Explore the notebooks in this repository for in-depth explanations and exercises.
* Practice writing small scripts and functions daily.
* Read the official [Python tutorial](https://docs.python.org/3/tutorial/) and [PEP 8](https://peps.python.org/pep-0008/) style guide.
