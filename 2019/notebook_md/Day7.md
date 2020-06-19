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
df_data = pd.read_csv('Day7-input.txt',header=None).T
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
def opcode_3(array,param,val):
    #array[param] = 1
    array[param] = val
```

```python
def opcode_4(array,param,mode):
    if mode == 0:
        print("output from code: ",array[param])
        return array[param]
    elif mode == 1:
        print("output from code: ",param)
        return param
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
def Intcode(data,ph,inp,ctr=None,return_n=False,n=0):
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
    n_inp = 0
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
                n_inp+=1
                if n_inp == 1 and ctr==None:
                    val = ph
                if n_inp == 2 or ctr=='on':
                    val = inp
                parm = data[n+1]
                opcode_3(data,parm,val)
                n = n+2
            if int(inst) == 4:
                mode = 0
                parm = data[n+1]
                rtrn = opcode_4(data,parm,mode)
                if return_n:
                    return rtrn,n+2
                else:
                    return rtrn
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
                rtrn = opcode_4(data,parm,mode[0])
                if return_n:
                    return rtrn,n+2
                else:
                    return rtrn
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
def thruster(dat,ph_set):
    output = []
    for i,p in enumerate(ph_set):
        if i == 0:
            inp = 0
        else:
            inp = output[i-1]
        res = Intcode(dat,p,inp)
        output.append(res)
    return output[-1]
```

```python jupyter={"outputs_hidden": true}
import itertools
thr_values = []
for p_comb in itertools.permutations([4,3,2,1,0]):
    thr_values.append(thruster(data,list(p_comb)))
```

```python
# solution
max(thr_values)
```

## Part-2

```python
def thruster_with_feedback(dat,ph_set):
    output = None
    flag = True
    dat_list = [dat.copy(),dat.copy(),dat.copy(),dat.copy(),dat.copy()]
    nn = np.array([0,0,0,0,0])
    out_list = []
    while True:
        for i,p in enumerate(ph_set):
            d = dat_list[i]
            if i == 0 and output == None:
                inp = 0
            else:
                inp = output
            if flag:
                output,nn[i] = Intcode(d,p,inp,return_n=True)
            else:
                output,nn[i] = Intcode(d,p,inp,ctr='on',return_n=True,n=nn[i])    
        flag = False
        if output == 'halt':
            break
        else:
            out_list.append(output)
    return out_list[-1]
```

```python
import itertools
thr_values = []
t_dat1 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
t_dat2 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
p_comb = [9,7,8,5,6]
thruster_with_feedback(t_dat2,p_comb)
```

```python jupyter={"outputs_hidden": true}
import itertools
thr_values = []
for p_comb in itertools.permutations([9,8,7,6,5]):
    thr_values.append(thruster_with_feedback(data,list(p_comb)))
```

```python
max(thr_values)
```

```python

```
