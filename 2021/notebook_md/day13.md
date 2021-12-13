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
ll = []
with open('input/day13.txt') as f:
    for d in f.readlines():
        l = d.strip()
        if not l:
            coords = ll
            ll = []
            continue
        ll.append(l)
    inst_ = ll
```

```python
inst = [d.split()[-1].split('=') for d in inst_]
```

```python
def getSheet(pos,size):
    sheet = np.zeros((size,size),int)
    for c in pos:
        x,y = map(int,c.split(','))
        sheet[y,x] = 1
    return sheet
```

```python
def fold(arr,n,ax):
    for i in range(n):
        r1 = i
        r2 = 2*n - i
        if ax == 'y':
            arr[r1] += arr[r2]
        else:
            arr[:,r1] += arr[:,r2]
    if ax == 'y':
        return arr[:n,:]
    else:
        return arr[:,:n]
```

```python
sheet = getSheet(coords,10000)
```

```python
for f in inst:
    ax, n = f
    sheet = fold(sheet,int(n),ax)
    break
```

```python
#assert (sheet >=1).sum() == 17,"WRONG!"
```

```python
print("Dots after first fold is",(sheet >=1).sum())
```

### Part 2

```python
sheet = getSheet(coords,10000)
```

```python
for f in inst:
    ax, n = f
    sheet = fold(sheet,int(n),ax)
```

```python
R,C = sheet.shape
for i in range(R):
    for j in range(C):
        if sheet[i,j] > 0:
            print('*',end='')
        else:
            print(' ',end='')
    print('\n',end='')
```
