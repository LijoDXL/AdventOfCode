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
def opcode_1(array,param,mode,base=None):
    res = 0
    for p,m in zip(param,mode):
        if m == 0:
            res+=array[p]
        if m == 1:
            res+=p
        if m == 2:
            res+=array[base+p]
    return res
```

```python
def opcode_2(array,param,mode,base=None):
    res = 1
    for p,m in zip(param,mode):
        if m == 0:
            res*=array[p]
        if m == 1:
            res*=p
        if m == 2:
            res*=array[base+p]
    return res
```

```python
def opcode_3(array,param,val=1,mode=None,base=None):
    #array[param] = 1
    if mode == 2:
        array[base+param] = val
    else:
        array[param] = val
```

```python
def opcode_4(array,param,mode,base=None):
    if mode == 0:
        #print("output from code: ",array[param])
        return array[param]
    elif mode == 1:
        #print("output from code: ",param)
        return param
    elif mode == 2:
        #print("output from code: ",array[base+param])
        return array[base+param]
    else:
        print("unknown mode")
```

```python
def opcode_5(array,param,mode,base=None):
    assert len(mode),2
    if mode[0] == 0:
        p = array[param[0]]
    if mode[0] == 1:
        p = param[0]
    if mode[0] == 2:
        p = array[base+param[0]]
    if p != 0:
        if mode[1] == 0:
            return array[param[1]]
        if mode[1] == 1:
            return param[1]
        if mode[1] == 2:
            return array[base+param[1]]
    if p == 0:
        return 0
```

```python
def opcode_6(array,param,mode,base=None):
    assert len(mode),2
    if mode[0] == 0:
        p = array[param[0]]
    if mode[0] == 1:
        p = param[0]
    if mode[0] == 2:
        p = array[base+param[0]]
    if p == 0:
        if mode[1] == 0:
            return array[param[1]]
        if mode[1] == 1:
            return param[1]
        if mode[1] == 2:
            return array[base+param[1]]
    if p != 0:
        return 0
```

```python
def opcode_7(array,param,mode,base=None):
    assert len(mode),3
    if mode[0] == 0:
        p1 = array[param[0]]
    if mode[0] == 1:
        p1 = param[0]
    if mode[0] == 2:
        p1 = array[base+param[0]]
    if mode[1] == 0:
        p2 = array[param[1]]
    if mode[1] == 1:
        p2 = param[1]
    if mode[1] == 2:
        p2 = array[base+param[1]]
    if p1 < p2:
        if mode[2] == 2:
            array[base+param[2]] = 1
        else:
            array[param[2]] = 1
    else:
        if mode[2] == 2:
            array[base+param[2]] = 0
        else:
            array[param[2]] = 0
```

```python
def opcode_8(array,param,mode,base=None):
    assert len(mode),3
    if mode[0] == 0:
        p1 = array[param[0]]
    if mode[0] == 1:
        p1 = param[0]
    if mode[0] == 2:
        p1 = array[base+param[0]]
    if mode[1] == 0:
        p2 = array[param[1]]
    if mode[1] == 1:
        p2 = param[1]
    if mode[1] == 2:
        p2 = array[base+param[1]]
    if p1 == p2:
        if mode[2] == 2:
            array[base+param[2]] = 1
        else:
            array[param[2]] = 1
    else:
        if mode[2] ==2:
            array[base+param[2]] = 0
        else:
            array[param[2]] = 0
```

```python
def opcode_9(array,param,mode,base=None):
    if mode == 0:
        return base+array[param]
    elif mode == 1:
        return base+param
    elif mode == 2:
        return base+array[base+param]
    else:
        print("unknown mode")
```

```python
def Intcode(data,inp=1,return_n=False,n=0,b=0):
    '''
    Parameters:
    ============
    data: array
    inp: input to be provided
    return_n: return the current reading point (also returns b)
    n: memory point from where reading should resume
    '''
    while True:
        mode = []
        inst = str(data[n])
        #print(inst)
        ndig = len(inst)
        if int(inst[-2:]) == 99:
            if return_n:
                return 'halt','halt','halt'
            break
        if ndig == 1:
            if int(inst) == 3:
                #n_inp+=1
                #if n_inp == 1 and ctr==None:
                #    val = ph
                #if n_inp == 2 or ctr=='on':
                #    val = inp
                parm = data[n+1]
                opcode_3(data,parm,mode=0,base=b,val=inp)
                n = n+2
            if int(inst) == 4:
                mode = 0
                parm = data[n+1]
                rtrn = opcode_4(data,parm,mode,base=b)
                if return_n:
                    return rtrn,n+2,b
                else:
                    return rtrn
                n = n+2
            if int(inst) == 1:
                mode.extend([0,0,0])
                parm = data[n+1:n+4]
                add = opcode_1(data,parm[:-1],mode[:-1],base=b)
                if mode[-1] == 0:
                    data[parm[-1]] = add
                if mode[-1] == 2:
                    data[b+parm[-1]] = add
                n = n+4
            if int(inst) == 2:
                mode.extend([0,0,0])
                parm = data[n+1:n+4]
                mult = opcode_2(data,parm[:-1],mode[:-1],base=b)
                if mode[-1] == 0:
                    data[parm[-1]] = mult
                if mode[-1] == 2:
                    data[b+parm[-1]] = mult
                n = n+4
            if int(inst) == 5:
                mode.extend([0,0])
                parm = data[n+1:n+3]
                mv = opcode_5(data,parm,mode,base=b)
                if mv == 0:
                    n = n+3
                if mv != 0:
                    n = mv
            if int(inst) == 6:
                mode.extend([0,0])
                parm = data[n+1:n+3]
                mv = opcode_6(data,parm,mode,base=b)
                if mv == 0:
                    n = n+3
                if mv != 0:
                    n = mv
            if int(inst) == 7:
                mode.extend([0,0,0])
                parm = data[n+1:n+4]
                opcode_7(data,parm,mode,base=b)
                n = n+4
            if int(inst) == 8:
                mode.extend([0,0,0])
                parm = data[n+1:n+4]
                opcode_8(data,parm,mode,base=b)
                n = n+4
            if int(inst) == 9:
                mode = 0
                parm = data[n+1]
                b = opcode_9(data,parm,mode,base=b)
                #print("small b is:",b)
                n = n+2
            #print("small",parm)
        if ndig > 1:
            opcode = int(inst[-2:])
            if ndig-2 == 3:
                mode.extend([int(i) for i in inst[:-2]])
            if ndig-2 == 2:
                mode.extend([0])
                mode.extend([int(i) for i in inst[:-2]])
            if ndig-2 == 1:
                mode.extend([0,0])
                mode.extend([int(i) for i in inst[:-2]])
            mode = mode[::-1]
            parm = data[n+1:n+4]
            #print("mode",mode)
            if opcode == 1:
                add = opcode_1(data,parm[:-1],mode[:-1],base=b)
                if mode[-1] == 0:
                    data[parm[-1]] = add
                if mode[-1] == 2:
                    data[b+parm[-1]] = add
                n = n+4
            if opcode == 2:
                mult = opcode_2(data,parm[:-1],mode[:-1],base=b)
                if mode[-1] == 0:
                    data[parm[-1]] = mult
                if mode[-1] == 2:
                    data[b+parm[-1]] = mult
                n = n+4
            if opcode == 3:
                parm = data[n+1]
                opcode_3(data,parm,mode=mode[0],base=b,val=2)
                n = n+2
            if opcode == 4:
                parm = data[n+1]
                rtrn = opcode_4(data,parm,mode[0],base=b)
                if return_n:
                    return rtrn,n+2,b
                else:
                    return rtrn
                n = n+2
            if opcode == 5:
                parm = data[n+1:n+3]
                mv = opcode_5(data,parm,mode,base=b)
                if mv == 0:
                    n = n+3
                if mv != 0:
                    n = mv
            if opcode == 6:
                parm = data[n+1:n+3]
                mv = opcode_6(data,parm,mode,base=b)
                if mv == 0:
                    n = n+3
                if mv != 0:
                    n = mv
            if opcode == 7:
                opcode_7(data,parm,mode,base=b)
                n = n+4
            if opcode == 8:
                opcode_8(data,parm,mode,base=b)
                n = n+4
            if opcode == 9:
                parm = data[n+1]
                b = opcode_9(data,parm,mode[0],base=b)
                n = n+2
```

```python
df_data = pd.read_csv('Day13-input.txt',header=None).T
```

```python
data_org = df_data.values.copy().flatten()
```

```python
data = np.zeros((400000000),dtype=int)
for i in range(len(data_org)):
    data[i] = data_org[i]
```

```python
data_game = data.copy()
```

```python
outputs = []
n_val,b_val = 0,0
while True:
    out_a,n_val,b_val = Intcode(data,inp=1,return_n=True,n=n_val,b=b_val)
    if out_a == 'halt':
        break
    out_b,n_val,b_val = Intcode(data,inp=1,return_n=True,n=n_val,b=b_val)
    out_c,n_val,b_val = Intcode(data,inp=1,return_n=True,n=n_val,b=b_val)
    outputs.append((out_a,out_b,out_c))
```

```python
blocks = [1 if x[2] == 2 else 0 for x in outputs]
# solution to part 1
blocks.count(1)
```

## Part-2

```python
# for animation
max_x = np.array([x for (x,y,v) in outputs]).max()
max_y = np.array([y for (x,y,v) in outputs]).max()
game_screen = np.zeros((max_y+1,max_x+1))
for (x,y,v) in outputs:
    game_screen[y,x] = v
import matplotlib.pyplot as plt
plt.matshow(game_screen)
plt.savefig('plots/day13_ArcadeGame_000.png',bbox_inches='tight')
plt.close()
```

```python
data_game[0] = 2
```

```python
n_val,b_val = 0,0
move = 0
pad_pos,ball_pos = (0,0),(0,0)
cnt = 0
while True:
    x,n_val,b_val = Intcode(data_game,inp=move,return_n=True,n=n_val,b=b_val)
    if x == 'halt':
        break
    y,n_val,b_val = Intcode(data_game,inp=move,return_n=True,n=n_val,b=b_val)
    ID,n_val,b_val = Intcode(data_game,inp=move,return_n=True,n=n_val,b=b_val)
    if ID == 3:
        pad_pos = (x,y)
    if ID == 4:
        ball_pos = (x,y)
    if pad_pos[0] < ball_pos[0]:
        move = 1
    elif pad_pos[0] > ball_pos[0]:
        move = -1
    else:
        move = 0
    if x == -1 and y == 0:
        print("Score: ",ID)
    else:
        game_screen[y,x] = ID
        cnt+=1
        plt.matshow(game_screen)
        plt.savefig(f'plots/day13_ArcadeGame_{cnt:03d}.png',bbox_inches='tight')
        plt.close()
```

```python

```

```python

```

```python

```

```python

```

```python

```
