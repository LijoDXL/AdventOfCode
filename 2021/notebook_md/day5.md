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
with open('input/day5.txt') as f:
    data = [f.strip().split(' -> ') for  f in f.readlines()]
```

```python
data = [[d.split(',') for d in i] for i in data]
```

```python
# horizontal
hor = [d for d in data if d[0][1] == d[1][1]]
```

```python
# vertical
ver = [d for d in data if d[0][0] == d[1][0]]
```

```python
grids = np.zeros((10000,10000))
```

```python
for h in hor:
    y = int(h[0][1])
    x1_ = int(h[0][0])
    x2_ = int(h[1][0])
    if x1_>x2_:
        x1=x2_
        x2=x1_
    else:
        x1=x1_
        x2=x2_
    grids[y,x1:x2+1]+=1
```

```python
for v in ver:
    x = int(v[0][0])
    y1_ = int(v[0][1])
    y2_ = int(v[1][1])
    if y1_>y2_:
        y1=y2_
        y2=y1_
    else:
        y1=y1_
        y2=y2_
    grids[y1:y2+1,x]+=1
```

```python
#assert (grids>=2).sum() == 5,"WRONG!"
```

```python
(grids>=2).sum()
```

### part-2

```python
def isDiag(vals):
    x1 = int(vals[0][0]);x2 = int(vals[1][0])
    y1 = int(vals[0][1]);y2 = int(vals[1][1])
    slope = (y2-y1)/(x2-x1)
    if abs(slope) == 1:
        return True
    else:
        return False
```

```python
dsel = ver+hor
rest = [d for d in data if d not in dsel]
diags = [v for v in rest if isDiag(v)]
```

```python
def markDiags(vals):
    x1 = int(vals[0][0]);x2 = int(vals[1][0])
    y1 = int(vals[0][1]);y2 = int(vals[1][1])
    x = x1
    y = y1
    points = [[x,y]]
    while (x,y) != (x2,y2):
        hstep = -1
        vstep = -1
        if x2 > x1:
            hstep = 1
        if y2 > y1:
            vstep = 1
        x+=hstep
        y+=vstep
        points.append([x,y])
    return points
```

```python
for d in diags:
    for i in markDiags(d):
        grids[i[1],i[0]] += 1
```

```python
#assert (grids>=2).sum() == 12,"WRONG!"
```

```python
(grids>=2).sum()
```

```python

```
