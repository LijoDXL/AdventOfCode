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
with open('inputs/day5.txt') as f:
    idList = f.readlines()
idList = [l.strip() for l in idList]
```

```python
def getRow(data):
    low,high = 0,127
    mid = ((high-low)+1)/2
    for i,c in enumerate(data[:-3]):
        if c == 'F':
            high = low+mid-1
        elif c == 'B':
            low = low+mid
        else:
            raise ValueError("unrecognized character")
        mid = ((high-low)+1)/2
    assert low == high
    row = high
    return row
```

```python
def getCol(data):
    low,high = 0,7
    mid = ((high-low)+1)/2
    for i,c in enumerate(data[-3:]):
        if c == 'L':
            high = low+mid-1
        elif c == 'R':
            low = low+mid
        else:
            raise ValueError("unrecognized character")
        mid = ((high-low)+1)/2
    assert low == high
    col = high
    return col
```

```python
def getSeatID(data):
    r = getRow(data)
    c = getCol(data)
    return r*8+c
```

```python
ex1 = 'FBFBBFFRLR'
ex2 = 'BFFFBBFRRR'
ex3 = 'FFFBBBFRRR'
ex4 = 'BBFFBBFRLL'
assert getSeatID(ex1) == 357
assert getSeatID(ex2) == 567
assert getSeatID(ex3) == 119
assert getSeatID(ex4) == 820
```

```python
sID = []
for i in idList:
    sID.append(getSeatID(i))
print('maximum seat ID is:',max(sID))
```

## Part 2

```python
sID = sorted(map(int,sID))
myseat = set(range(sID[0],sID[-1]+1)) - set(sID)
print(myseat)
```
