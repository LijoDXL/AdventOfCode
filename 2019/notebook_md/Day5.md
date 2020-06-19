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
df_data = pd.read_csv('Day5-input.txt',header=None).T
```

```python
data = df_data.values.copy().flatten()
```

```python
def opcode_1(array,param,mode):
    res = 0
    for p,m in zip(param,mode):
        if m == 0:
            res+=array[p]
        if m == 1:
            res+=p
    return res
```

```python
def opcode_2(array,param,mode):
    res = 1
    for p,m in zip(param,mode):
        if m == 0:
            res*=array[p]
        if m == 1:
            res*=p
    return res
```

```python
def opcode_3(array,param):
    #array[param] = 1
    array[param] = 5
```

```python
def opcode_4(array,param,mode):
    if mode == 0:
        print("output from code: ",array[param])
    elif mode == 1:
        print("output from code: ",param)
    else:
        print("unknown mode")
```

```python
def opcode_5(array,param,mode):
    assert len(mode),2
    if mode[0] == 0:
        p = array[param[0]]
    if mode[0] == 1:
        p = param[0]
    if p != 0:
        if mode[1] == 0:
            return array[param[1]]
        if mode[1] == 1:
            return param[1]
    if p == 0:
        return 0
```

```python
def opcode_6(array,param,mode):
    assert len(mode),2
    if mode[0] == 0:
        p = array[param[0]]
    if mode[0] == 1:
        p = param[0]
    if p == 0:
        if mode[1] == 0:
            return array[param[1]]
        if mode[1] == 1:
            return param[1]
    if p != 0:
        return 0
```

```python
def opcode_7(array,param,mode):
    assert len(mode),3
    if mode[0] == 0:
        p1 = array[param[0]]
    if mode[0] == 1:
        p1 = param[0]
    if mode[1] == 0:
        p2 = array[param[1]]
    if mode[1] == 1:
        p2 = param[1]
    if p1 < p2:
        array[param[2]] = 1
    else:
        array[param[2]] = 0
```

```python
def opcode_8(array,param,mode):
    assert len(mode),3
    if mode[0] == 0:
        p1 = array[param[0]]
    if mode[0] == 1:
        p1 = param[0]
    if mode[1] == 0:
        p2 = array[param[1]]
    if mode[1] == 1:
        p2 = param[1]
    if p1 == p2:
        array[param[2]] = 1
    else:
        array[param[2]] = 0
```

```python
n=0
data = df_data.values.copy().flatten()
while True:
    mode = []
    inst = str(data[n])
    #print(inst)
    ndig = len(inst)
    if int(inst[-2:]) == 99:
        break
    if ndig == 1:
        if int(inst) == 3:
            parm = data[n+1]
            opcode_3(data,parm)
            n = n+2
        if int(inst) == 4:
            mode = 0
            parm = data[n+1]
            opcode_4(data,parm,mode)
            n = n+2
        if int(inst) == 1:
            mode.extend([0,0,0])
            parm = data[n+1:n+4]
            add = opcode_1(data,parm[:-1],mode[:-1])
            data[parm[-1]] = add
            n = n+4
        if int(inst) == 2:
            mode.extend([0,0,0])
            parm = data[n+1:n+4]
            mult = opcode_2(data,parm[:-1],mode[:-1])
            data[parm[-1]] = mult
            n = n+4
        #print(parm)
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
            add = opcode_1(data,parm[:-1],mode[:-1])
            data[parm[-1]] = add
            n = n+4
        if opcode == 2:
            mult = opcode_2(data,parm[:-1],mode[:-1])
            data[parm[-1]] = mult
            n = n+4
        if opcode == 4:
            parm = data[n+1]
            opcode_4(data,parm,mode[0])
            n = n+2    
        #print(parm)
```

## Part-2

```python
n=0
data = df_data.values.copy().flatten()
while True:
    mode = []
    inst = str(data[n])
    #print(inst)
    ndig = len(inst)
    if int(inst[-2:]) == 99:
        break
    if ndig == 1:
        if int(inst) == 3:
            parm = data[n+1]
            opcode_3(data,parm)
            n = n+2
        if int(inst) == 4:
            mode = 0
            parm = data[n+1]
            opcode_4(data,parm,mode)
            n = n+2
        if int(inst) == 1:
            mode.extend([0,0,0])
            parm = data[n+1:n+4]
            add = opcode_1(data,parm[:-1],mode[:-1])
            data[parm[-1]] = add
            n = n+4
        if int(inst) == 2:
            mode.extend([0,0,0])
            parm = data[n+1:n+4]
            mult = opcode_2(data,parm[:-1],mode[:-1])
            data[parm[-1]] = mult
            n = n+4
        if int(inst) == 5:
            mode.extend([0,0])
            parm = data[n+1:n+3]
            mv = opcode_5(data,parm,mode)
            if mv == 0:
                n = n+3
            if mv != 0:
                n = mv
        if int(inst) == 6:
            mode.extend([0,0])
            parm = data[n+1:n+3]
            mv = opcode_6(data,parm,mode)
            if mv == 0:
                n = n+3
            if mv != 0:
                n = mv
        if int(inst) == 7:
            mode.extend([0,0,0])
            parm = data[n+1:n+4]
            opcode_7(data,parm,mode)
            n = n+4
        if int(inst) == 8:
            mode.extend([0,0,0])
            parm = data[n+1:n+4]
            opcode_8(data,parm,mode)
            n = n+4
        #print(parm)
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
            add = opcode_1(data,parm[:-1],mode[:-1])
            data[parm[-1]] = add
            n = n+4
        if opcode == 2:
            mult = opcode_2(data,parm[:-1],mode[:-1])
            data[parm[-1]] = mult
            n = n+4
        if opcode == 4:
            parm = data[n+1]
            opcode_4(data,parm,mode[0])
            n = n+2
        if opcode == 5:
            parm = data[n+1:n+3]
            mv = opcode_5(data,parm,mode)
            if mv == 0:
                n = n+3
            if mv != 0:
                n = mv
        if opcode == 6:
            parm = data[n+1:n+3]
            mv = opcode_6(data,parm,mode)
            if mv == 0:
                n = n+3
            if mv != 0:
                n = mv
        if opcode == 7:
            opcode_7(data,parm,mode)
            n = n+4
        if opcode == 8:
            opcode_8(data,parm,mode)
            n = n+4
        #print(parm)
```

```python

```
