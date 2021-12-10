---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.0
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

```python
import numpy as np
```

```python
with open('input/day7.txt') as f:
    data = [int(x) for x in f.readline().strip().split(',')]
```

```python
cntr = np.median(data)
```

```python
fuel = sum([abs(cntr-x) for x in data])
```

```python
#assert fuel == 37, "WRONG"
```

```python
print("the total fuel is",fuel)
```

### Part 2

```python
## Part-2 is inspired from Jonathan paulson youtube video
# I failed to find derivative of the cost function to minimize it.
# video showed me that brute force takes less time
```

```python
def sum_n(n):
    return n*(n+1)//2
```

```python
a = min(data);b=max(data)
```

```python
best = 9e10
for i in range(a,b):
    score = 0
    for d in data:
        score += sum_n(abs(d-i))
    if score < best:
        best = score
```

```python
#assert best == 168,"WRONG!"
```

```python
print("the fuel is",best)
```

```python

```
