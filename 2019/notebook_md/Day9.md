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
df_data = pd.read_csv('Day9-input.txt',header=None).T
```

```python
data = df_data.values.copy().flatten()
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
        print("output from code: ",array[param])
        return array[param]
    elif mode == 1:
        print("output from code: ",param)
        return param
    elif mode == 2:
        print("output from code: ",array[base+param])
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
def Intcode(data,inp=1,ctr=None,return_n=False,n=0):
    '''
    Parameters:
    ============
    data: array
    ph: phase setting
    inp: input to be provided
    ctr: if ctr is 'on', feebback set's in
    return_n: return the current reading point
    n: memoery point from where reading should resume
    '''
    n_inp = 0 # to check if input is 1st time or 2nd
    b = 0
    while True:
        mode = []
        inst = str(data[n])
        #print(inst)
        ndig = len(inst)
        if int(inst[-2:]) == 99:
            if return_n:
                return 'halt',-999
            break
        if ndig == 1:
            if int(inst) == 3:
                #n_inp+=1
                #if n_inp == 1 and ctr==None:
                #    val = ph
                #if n_inp == 2 or ctr=='on':
                #    val = inp
                parm = data[n+1]
                opcode_3(data,parm,mode=0,base=b,val=2)
                n = n+2
            if int(inst) == 4:
                mode = 0
                parm = data[n+1]
                rtrn = opcode_4(data,parm,mode,base=b)
                #if return_n:
                #    return rtrn,n+2
                #else:
                #    return rtrn
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
                #if return_n:
                #    return rtrn,n+2
                #else:
                #    return rtrn
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
                #print("big b before is:",b)
                b = opcode_9(data,parm,mode[0],base=b)
                #print("big b after is:",b)
                n = n+2
            #print("big:",parm)
```

```python
data_extn = np.zeros((400000000),dtype=int)
#test_dat = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
for i in range(len(data)):
    data_extn[i] = data[i]
num = Intcode(data_extn,ctr=None,return_n=False,n=0)
```

## Part-2
* for part-2, add val=2 as arg for all opcode_3 function calls

```python

```
