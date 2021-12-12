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
data = np.genfromtxt('input/day11.txt',delimiter=1,dtype=int)
data
```

```python
R,C = data.shape
```

```python
def flash(arr,reset=False):
    flashed = []
    cnt = 0
    for r in range(R):
        for c in range(C):
            if arr[r,c] == 10:
                if reset:
                    arr[r,c] = 0
                    cnt += 1
                else:
                    flashed.append((r,c))
    return flashed,cnt
```

```python
def adjacentINC(arr,r,c):
    trig = []
    Rd = [0, 0, 1, -1, -1, 1, -1, 1]
    Cd = [1, -1, 0, 0, 1, 1, -1, -1]
    for i in range(8):
        rr = r+Rd[i]
        cc = c+Cd[i]
        if 0<=rr<R and 0<=cc<C and arr[rr,cc]<10:
            arr[rr,cc] += 1
            if arr[rr,cc] == 10:
                trig.append((rr,cc))
    return trig
```

```python
def process(arr):
    block = arr.copy()
    block = block+1
    flashed,_ = flash(block)
    trigger = []
    if flashed:
        for f in flashed:
            trigger = adjacentINC(block,f[0],f[1])
            while trigger:  # if flash triggered by another flash
                #print(trigger)
                tt = []
                for i in trigger:
                    #print(i)
                    flist = adjacentINC(block,i[0],i[1])
                    if flist:
                        tt.extend(flist)
                trigger  = tt
    _,cnt = flash(block,reset=True)
    return block,cnt
```

```python
def totFlashes(arr,n):
    fcnt = 0
    for _ in range(n):
        arr,n = process(arr)
        fcnt += n
        #print(state,'\n')
    return fcnt
```

```python
state = data.copy()
```

```python
#assert totFlashes(state,10) == 204,"WRONG!"
#assert totFlashes(state,100) == 1656,"WRONG!"
```

```python
ans = totFlashes(state,100)
print("Total flashes are",ans)
```

### Part 2

```python
arr = data.copy()
cnt = 0
while not (arr==0).all():
    arr,_ = process(arr)
    cnt += 1
```

```python
#assert cnt == 195,"WRONG!"
```

```python
print("Total sync happens at step:",cnt)
```

```python

```
