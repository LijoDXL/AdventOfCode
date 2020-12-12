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
def parseInput(fname):
    data = []
    rec = []
    with open(f'inputs/{fname}') as f:
        for line in f:
            if line.strip():
                rec.append(line.strip())
            else:
                data.append(rec)
                rec = []
    data.append(rec)
    return data
```

```python
data = parseInput('day6_ex1.txt')
cnt = 0
for i in range(len(data)):
    cnt+=len(set(''.join(data[i])))
assert cnt == 11
```

```python
data = parseInput('day6.txt')
cnt = 0
for i in range(len(data)):
    cnt+=len(set(''.join(data[i])))
print("The sum is: ",cnt)
```

## Part 2

```python
data = parseInput('day6_ex1.txt')
cnt = 0
for i in range(len(data)):
    cnt+=len(set.intersection(*[set(el) for el in data[i]]))
assert cnt == 6
```

```python
data = parseInput('day6.txt')
cnt = 0
for i in range(len(data)):
    cnt+=len(set.intersection(*[set(el) for el in data[i]]))
print("The sum is",cnt)
```

```python

```
