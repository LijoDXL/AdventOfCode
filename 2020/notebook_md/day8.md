---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.5.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
def readInst(fname):
    with open(f'inputs/{fname}.txt','r') as f:
        instr = f.readlines()
    return [f.strip() for f in instr]
```

```python
def doit(cmd,n,line,acc):
    if cmd == 'nop':
        return acc,line+1
    elif cmd == 'acc':
        return acc+n,line+1
    elif cmd == 'jmp':
        return acc,line+n
    else:
        raise ValueError("unrecognized command. Only nop, acc or jmp acceptable")
```

```python
def calAccum(instr):
    accum = 0
    l = 0
    lineExc = []
    c = instr[l]
    while l not in lineExc:
        c = instr[l]
        act,num = c.split()
        lineExc.append(l)
        accum,l = doit(act,int(num),l,accum)
    return accum
```

```python
instructn = readInst('day8_ex1')
acc = calAccum(instructn)
assert acc == 5
```

```python
instructn = readInst('day8')
acc = calAccum(instructn)
print("the value is: ",accum)
```

## Part-2

```python
instructn = readInst('day8_ex1')
```

```python
def calAccum2(instr):
    accum = 0
    l = 0
    lineExc = []
    c = instr[l]
    while l not in lineExc:
        c = instr[l]
        act,num = c.split()
        lineExc.append(l)
        accum,l = doit(act,int(num),l,accum)
        if l == len(instr):
            print("Natural termination!, The value of accum is",accum)
            break
    return accum
```

```python
def chngInstr(instr,line):
    c,n = instr.split()
    if c == 'nop':
        cmd = 'jmp'
    elif c == 'jmp':
        cmd = 'nop'
    else:
        pass
    newinstr = instructn.copy()
    newinstr[line] = " ".join(cmd,n)
    return newinstr
```

```python
def chngInstr(instr):
    i = 0
    while i <= len(instr):
        for j in range(i,len(instr)):
            c = instr[j]
            act,num = c.split()
            if act == 'nop' or act == 'jmp':
                chngInstr(act,j)
                i = j+1
                break
            else:
                raise ValueError("instruction not recognized")
                
    return instr
```

```python
for c in instructn:
    act = c.split()[0]
    if act == 'nop':
        
        
```
