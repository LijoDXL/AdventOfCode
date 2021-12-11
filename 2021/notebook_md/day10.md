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
with open('input/day10.txt') as f:
    data = [d.strip() for d in f.readlines()]
```

```python
points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
    }
```

```python
def mismatch(dat,getList=False):
    mylist = []
    for i in dat:
        if i in pair.values():
            mylist.append(i)
            #print(*mylist)
        else:
            if pair[i] == mylist[-1]:
                mylist.pop()
            else:
                #print('mismatch at',i)
                return i
    if getList:
        return mylist
    return None
```

```python
pair = {}
pair['>'] = '<'
pair[')'] = '('
pair[']'] = '['
pair['}'] = '{'
```

```python
score = []
incmplt = []
for d in data:
    c = mismatch(d)
    if c is not None:
        score.append(points[c])
    else:
        incmplt.append(d)
```

```python
#assert sum(score) == 26397,"WRONG!"
```

```python
print("the score is",sum(score))
```

### Part 2

```python
closing = {}
closing['<'] = '>'
closing['('] = ')'
closing['['] = ']'
closing['{'] = '}'
```

```python
points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
    }
```

```python
def getScore(line):
    comp = [closing[c] for c in line[::-1]]
    score = 0
    for c in comp:
        score *= 5
        score += points[c]
    return score
```

```python
scoreBoard = []
for d in incmplt:
    ml = mismatch(d,getList=True)
    s = getScore(ml)
    scoreBoard.append(s)
```

```python
#assert np.median(scoreBoard) == 288957,"WRONG!"
```

```python
print("The middle score is",np.median(scoreBoard))
```

```python

```
