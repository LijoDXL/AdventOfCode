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
# this solution is inspired from https://www.youtube.com/watch?v=fHlWM8CIrlI
```

```python
from collections import defaultdict
```

```python
with open('input/day6.txt') as f:
    data = [int(x) for x in f.readline().strip().split(',')]
```

```python
def fishCount(initState,ndays):
    X = {}
    for x in initState:
        if x not in X:
            X[x] = 1
        else:
            X[x] += 1
    for _ in range(ndays):
        Y = defaultdict(int)
        for x,cnt in X.items():
            if x == 0:
                Y[6] += cnt 
                Y[8] += cnt
            else:
                Y[x-1] += cnt
        X = Y
    return sum(X.values())
```

```python
#assert fishCount(data,18) == 26,"WRONG!"
```

```python
#assert fishCount(data,80) == 5934,"WRONG!"
```

```python
print("Total fish will be:",fishCount(data,80))
```

### Part-2

```python
#assert fishCount(data,256) == 26984457539, "WRONG!"
```

```python
print("Total fish will be:",fishCount(data,256))
```

```python

```
