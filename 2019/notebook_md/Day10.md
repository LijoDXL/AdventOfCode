---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.2.4
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
```

```python
pos = []
with open('Day10-input.txt','r') as f:
    y = 0
    for line in f.readlines():
        x = 0
        for l in line:
            if l == '#':
                pos.append((x,y))
            x+=1
        y+=1        
```

```python
arr = np.zeros((y,x),dtype=int)
xx,yy = np.meshgrid(range(x),range(y))
for (x,y) in pos:
    arr[y,x] = 1
```

```python
plt.imshow(arr)
plt.scatter(xx,yy,color='k',s=8)
plt.plot([3,4],[4,0],'k--')
```

```python
count = []
for i in range(len(pos)):
    detect = len(pos)-1
    x1,y1 = pos[i]
    for j in range(len(pos)):
        block = 0
        x2,y2 = pos[j]
        if (x2,y2) == (x1,y1):
            continue
        dist = np.sqrt((x2-x1)**2+(y2-y1)**2)
        if x2 == x1:
            for (x0,y0) in pos:
                if (x0,y0) == (x1,y1) or (x0,y0) == (x2,y2):
                    continue
                if x0 == x2:
                    if abs(y0-y1) < dist:
                        if (y1-y2)/abs(y1-y2) == (y1-y0)/abs(y1-y0):
                            #print(f"off-limits,{x2},{y2}")
                            block+=1
                if block:
                    break
        else:
            slope = (y2-y1)/(x2-x1)
            for (x0,y0) in pos:
                if (x0,y0) == (x1,y1) or (x0,y0) == (x2,y2):
                    continue
                if slope*(x0-x2)+y2-y0 == 0:
                    if np.sqrt((x0-x1)**2+(y0-y1)**2) < dist:
                        if (x1-x2)/abs(x1-x2) == (x1-x0)/abs(x1-x0):
                            #print(f"off-limits,{x2},{y2}")
                            block+=1
                if block:
                    break
        if block != 0:
            detect-=1
    count.append(detect)
```

```python
print("maximum asteroid detectable is:",max(count))
```

```python
loc = np.array(count).argmax()
print("maximum asteroid can be detected at:",pos[loc])
```

## Part-2

```python
best_pos = pos[loc]
x1,y1 = best_pos
```

```python
plt.imshow(arr)
plt.scatter(xx,yy,color='k',s=8)
plt.scatter([x for (x,y) in pos],[y for (x,y) in pos],color='b',s=8,marker='*')
plt.plot(x1,y1,'r',marker='d')
```

```python
def detect_targets(pos,x1=x1,y1=y1):
    detect = len(pos)-1
    detected_ast = []
    for j in range(len(pos)):
        block = 0
        x2,y2 = pos[j]
        if (x2,y2) == (x1,y1):
            continue
        dist = np.sqrt((x2-x1)**2+(y2-y1)**2)
        if x2 == x1:
            for (x0,y0) in pos:
                if (x0,y0) == (x1,y1) or (x0,y0) == (x2,y2):
                    continue
                if x0 == x2:
                    if abs(y0-y1) < dist:
                        if (y1-y2)/abs(y1-y2) == (y1-y0)/abs(y1-y0):
                            #print(f"off-limits,{x2},{y2}")
                            block+=1
                if block:
                    break
        else:
            slope = (y2-y1)/(x2-x1)
            for (x0,y0) in pos:
                if (x0,y0) == (x1,y1) or (x0,y0) == (x2,y2):
                    continue
                if slope*(x0-x2)+y2-y0 == 0:
                    if np.sqrt((x0-x1)**2+(y0-y1)**2) < dist:
                        if (x1-x2)/abs(x1-x2) == (x1-x0)/abs(x1-x0):
                            #print(f"off-limits,{x2},{y2}")
                            block+=1
                if block:
                    break
        if block != 0:
            detect-=1
        else:
            detected_ast.append((x2,y2))
    return detect,detected_ast
```

```python
num,ast_pos = detect_targets(pos)
assert len(ast_pos),num
```

```python
plt.imshow(arr)
plt.scatter(xx,yy,color='k',s=8)
plt.scatter([x for (x,y) in pos],[y for (x,y) in pos],color='b',s=8,marker='*')
plt.scatter([x for (x,y) in ast_pos],[y for (x,y) in ast_pos],color='r',s=8,marker='*')
plt.plot(x1,y1,'r',marker='d')
plt.yticks(np.arange(0,25,5))
plt.ylim(20.5,-0.5)
plt.savefig(f'plots/day10_pew000.png',bbox_inches='tight')
```

```python
angles = [np.rad2deg(np.arctan2(y_val-y1,x_val-x1)) for (x_val,y_val) in ast_pos]
angles = [90+a for a in angles]
```

* test
---
"""i = 0
for p in ast_pos:
    if p == (10,4):
        break
    i+=1
angles[i]"""

```python
angles_360 = [360+ang if ang < 0 else ang for ang in angles]
```

```python
ast_pos = np.array(ast_pos)
angles_360 = np.array(angles_360)
```

```python
ast_pos_sorted = ast_pos[np.argsort(angles_360)]
```

```python
# solution
print("the 200th asteroid to be distroyed is at:",ast_pos_sorted[199])
```

```python
# answer to submit
print(ast_pos_sorted[199][0]*100+ast_pos_sorted[199][1])
```

## Bonus

```python
def plot_state(arr,pos_left):
    plt.imshow(arr)
    plt.scatter(xx,yy,color='k',s=8)
    plt.scatter([x for (x,y) in pos_left],[y for (x,y) in pos_left],color='b',s=8,marker='*')
    plt.plot(x1,y1,'r',marker='d')
    plt.yticks(np.arange(0,25,5))
    plt.ylim(20.5,-0.5)
```

```python
for i,(x,y) in enumerate(ast_pos_sorted):
    arr[y,x] = 0
    pos_left = ast_pos_sorted[i+1:]
    plot_state(arr,pos_left)
    plt.savefig(f'plots/day10_pew{i+1:03d}.png',bbox_inches='tight')
    plt.close()
```

```python

```
