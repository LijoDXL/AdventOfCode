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
import pandas as pd
import numpy as np
```

```python
df1 = pd.read_csv('Day3-input.txt',header=None,skipfooter=1,engine='python')
df2 = pd.read_csv('Day3-input.txt',header=None,skiprows=1,engine='python')
print("# of elements in wire1:", len(df1.columns))
print("# of elements in wire2:",len(df2.columns))
```

```python
# since both of them have same number of instructions, lets join
df = df1.append(df2,ignore_index=True)
df.head()
```

```python
# get an idea about the bounds(size) of grid required
l_bnd = df.loc[0,df.loc[0,:].str[0] == 'L'].str[1:].astype(int).sum()
r_bnd = df.loc[0,df.loc[0,:].str[0] == 'R'].str[1:].astype(int).sum()
u_bnd = df.loc[0,df.loc[0,:].str[0] == 'U'].str[1:].astype(int).sum()
d_bnd = df.loc[0,df.loc[0,:].str[0] == 'D'].str[1:].astype(int).sum()
print(f"left: {l_bnd}, right: {r_bnd}, top: {u_bnd}, bottom: {d_bnd}")
```

```python
def trace_wire(wire,grid,flag):
    holder = []
    posx = 2000 # I thought I typed in 20000, but hey it still works
    posy = 2000
    for i in wire:
        move=i[0]
        steps=int(i[1:])
        if move == 'R':
            if flag == 1:
                grid[posy,posx:posx+steps+1]=1
            else:
                grid[posy,posx:posx+steps+1]+=2
            for n,el in enumerate(grid[posy,posx:posx+steps+1]):
                if el%2 !=0 and el != 1:
                    #print('row:',posy,'col:',posx+n)
                    holder.append((posy,posx+n))
            posx+=steps
        elif move == 'L':
            if flag == 1:
                grid[posy,posx-steps:posx+1]=1
            else:
                grid[posy,posx-steps:posx+1]+=2
            for n,el in enumerate(grid[posy,posx-steps:posx+1]):
                if el%2 !=0 and el != 1:
                    #print('row:',posy,'col:',posx-steps+n)
                    holder.append((posy,posx-steps+n))
            posx-= steps
        elif move == 'U':
            if flag == 1:
                grid[posy-steps:posy+1,posx]=1
            else:
                grid[posy-steps:posy+1,posx]+=2
            for n,el in enumerate(grid[posy-steps:posy+1,posx]):
                if el%2 !=0 and el != 1:
                    #print('row:',posy-steps+n,'col:',posx)
                    holder.append((posy-steps+n,posx))
            posy-=steps
        elif move == 'D':
            if flag == 1:
                grid[posy:posy+steps+1,posx]=1
            else:
                grid[posy:posy+steps+1,posx]+=2
            for n,el in enumerate(grid[posy:posy+steps+1,posx]):
                if el%2 !=0 and el != 1:
                    #print('row:',posy+n,'col:',posx)
                    holder.append((posy+n,posx))
            posy+=steps
        else:
            print('Unknown move')
    return holder
```

```python
test1_w1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(',')
test1_w2 = "U62,R66,U55,R34,D71,R55,D58,R83".split(',')
test2_w1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(',')
test2_w2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(',')
```

```python
def closest(w1,w2):
    grid = np.zeros((40001,40001),dtype=int)
    _ = trace_wire(w1,grid,flag=1)
    inter = trace_wire(w2,grid,flag=2)
    dist = np.array([abs(2000-x)+abs(2000-y) for (x,y) in inter if x!=2000 and y!=2000]).min()
    return dist,inter
```

```python
dist,itr_points = closest(test1_w1,test1_w2)
assert dist,159
```

```python
dist,itr_points = closest(test2_w1,test2_w2)
assert dist,135
```

```python
dist,itr_points = closest(df.loc[0,:].values,df.loc[1,:].values)
```

```python
# solution
print("The closest intersection point is at a distance of", dist, "units")
```

## Part-2

```python
def steps(w,pt):    
    posx = 2000
    posy = 2000
    step_sum = 0
    cnt = 0
    flag = 1
    dest = pt
    while flag:
        el = w[cnt]
        move=el[0]
        steps=int(el[1:])
        if move == 'R':
            for i in range(1,steps+1):
                x=posx+i
                y=posy
                if (y,x) == dest:
                    flag = 0
                    posx = x
                    posy = y
                    break
            step_sum+=i
            posx = x
            posy = y
        elif move == 'L':
            for i in range(1,steps+1):
                x=posx-i
                y=posy
                if (y,x) == dest:
                    flag = 0
                    posx = x
                    posy = y
                    break
            step_sum+=i
            posx = x
            posy = y
        elif move == 'U':
            for i in range(1,steps+1):
                y=posy-i
                x=posx
                if (y,x) == dest:
                    flag = 0
                    posx = x
                    posy = y
                    break
            step_sum+=i
            posx = x
            posy = y
        elif move == 'D':
            for i in range(1,steps+1):
                y=posy+i
                x=posx
                if (y,x) == dest:
                    flag = 0
                    posx = x
                    posy = y
                    break
            step_sum+=i
            posx = x
            posy = y
        else:
            print('Unknown move')
        #print(y,x)
        cnt+=1
    return step_sum
```

```python
def min_steps(w1,w2):
    cntr = []
    dist,itr_points = closest(w1,w2)
    for i in itr_points[1:]:
        w1_steps = steps(w1,i)
        w2_steps = steps(w2,i)
        tot_steps = w1_steps+w2_steps
        cntr.append(tot_steps)
    return min(cntr)
```

```python
assert min_steps(test1_w1,test1_w2),610
assert min_steps(test2_w1,test2_w2),410
```

```python
# solution
min_steps(df.loc[0,:].values,df.loc[1,:].values)
```

```python

```
