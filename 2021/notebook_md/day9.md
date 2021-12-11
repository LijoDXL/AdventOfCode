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
with open('input/day9.txt') as f:
    data = [x.strip() for x in f.readlines()]
```

```python
r = len(data)
c = len(data[0])
```

```python
a = np.zeros((r,c))
```

```python
for i in range(r):
    for j in range(c):
        a[i,j] = int(data[i][j])
```

```python
def findMin(arr,i,j):
    """Thanks to Jonathan Paulson for the rr,cc method
    """
    mini = 10
    rr = [0,0,1,-1]
    cc = [1,-1,0,0]
    for p in range(4):
        rn = i+rr[p]
        cn = j+cc[p]
        if 0 <= rn < r and 0 <= cn < c:
            if arr[rn,cn] < mini:
                mini = arr[rn,cn]
                mpos = (rn,cn)
    return mini,mpos
```

```python
lp = []
lp_pos = []
for i in range(r):
    for j in range(c):
        if a[i,j] == 9:
            continue
        if a[i,j] == 0:
            lp.append(0)
            lp_pos.append((i,j))
            continue
        m,_ = findMin(a,i,j)
        if a[i,j] < m:
            lp.append(a[i,j])
            lp_pos.append((i,j))
```

```python
rlevel = [x+1 for x in lp]
```

```python
#assert sum(rlevel) == 15,"WRONG!"
```

```python
print("The sum is",sum(rlevel))
```

### part 2

```python
pos = {}
for  i in lp_pos:
    pos[i] = 0
```

```python
for i in range(r):
    for j in range(c):
        if a[i,j] == 9:
            continue
        k=i
        l=j
        while True:
            if (k,l) in lp_pos:
                pos[(k,l)] += 1
                break
            _,(k,l) = findMin(a,k,l)
```

```python
largest = sorted(pos.values())[-3:]
ans = 1
for x in largest:
    ans *= x
```

```python
assert ans == 1134, "WRONG!"
```

```python
print("The answer is:",ans)
```
