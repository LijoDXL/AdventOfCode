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
with open('input/day14.txt') as f:
    data = [d.strip() for d in f.readlines()]
```

```python
temp = data[0]
pairs = {}
for d in data[2:]:
    l,r = d.split(' -> ')
    pairs[l] = r
```

```python
def process(dat):
    growth = ''
    for i in range(len(dat)-1):
        el = dat[i:i+2]
        el_add = el[0]+pairs[el]
        growth += el_add
    growth+=el[-1]
    return growth
```

```python
D = temp
for _ in range(10):
    D = process(D)
```

```python
uniq = [D[0]]
for d in D[1:]:
    if d not in uniq:
        uniq.append(d)
```

```python
counts = {}
for e in uniq:
    counts[e] = D.count(e)
```

```python
count_sort = sorted(counts.values())
ans = count_sort[-1] - count_sort[0]
print(ans)
```

### Part 2

```python
from collections import defaultdict,Counter
```

```python
CN = Counter(temp)
```

```python
G = Counter()
for i in range(len(temp)-1):
    G[temp[i]+temp[i+1]] += 1
```

```python
for _ in range(40):
    A = Counter()
    for p in G:
        c = pairs[p[0]+p[1]]
        A[p[0]+c] += G[p[0]+p[1]]
        A[c+p[1]] += G[p[0]+p[1]]
        CN[c] += G[p[0]+p[1]]
    G = A
```

```python
(e1,n1) = CN.most_common()[0]
(e0,n0) = CN.most_common()[-1]
```

```python
n1-n0
```

```python

```
