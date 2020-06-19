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
```

```python
pos0_inp = np.array([[-4,-9,-3],[-13,-11,0],[-17,-7,15],[-16,4,2]])
vel0_inp = np.array([[0,0,0],[0,0,0],[0,0,0],[0,0,0]])
```

```python
pos0_test1 = np.array([[-1,0,2],[2,-10,-7],[4,-8,8],[3,5,-1]])
vel0_test1 = np.zeros_like(pos0_test1)
```

```python
pos0_test2 = np.array([[-8,-10,0],[5,5,10],[2,-7,3],[9,-8,-3]])
vel0_test2 = np.zeros_like(pos0_test2)
```

```python
def update(pos,vel):
    vel_ = []
    for i in range(4):
        dv = np.where(pos[i] > pos,-1,-999)
        dv = np.where(pos[i] < pos,1,dv)
        dv = np.where(pos[i] == pos,0,dv)
        vel_.append(dv.sum(axis=0))
    vel_n = np.vstack(vel_) + vel
    pos_n = pos+vel_n
    return pos_n,vel_n
```

```python
def energy(tsteps,p_in,v_in):
    p = pos0_inp
    v = vel0_inp
    for t in range(1,tsteps+1):
        p,v = update(p,v)
    return (np.abs(p).sum(axis=1) * np.abs(v).sum(axis=1)).sum()
```

```python
assert energy(100,pos0_test1,vel0_test1),179
```

```python
assert energy(100,pos0_test2,vel0_test2),1940
```

```python
# solution
energy(1000,pos0_inp,vel0_inp)
```

```python
p
```

## Part-2

```python
np.lcm(np.lcm(18,28),44)
```

```python
"=="*4
```

```python jupyter={"outputs_hidden": true}
p = pos0_test1
v = vel0_test1
#p_list = [p[np.newaxis,...]]
#v_list = [v[np.newaxis,...]]
#p_arr = np.vstack(p_list)
#v_arr = np.vstack(v_list)    
cnt = 0

for i in range(3):
    while True:
        p,v = update(p,v)
        cnt+=1
        v_flag = (v == vel0_test2).all()
        if v_flag:
            p_flag = (p == pos0_test2).all()
            if p_flag:
                print("   Match found in iteration #",cnt)
                print("position;\n",p,"\nvelocity;\n",v)
                break
            else:
                print("Velocity match but Position no match iteration #",cnt)
        else:
            print("No match found in iteration #",cnt)
```

```python
pos0_test2
```

```python

```
