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
from collections import defaultdict
```

```python
with open('input/day12ex3.txt') as f:
    data = [d.strip().split('-') for d in f.readlines()]
```

```python
s = start[0]
clist = conn[s]
while clist:
    for c in clist:
        asjdlkajds
    clist = conn[c]
```

```python
conn = defaultdict(list)
start = []
end = []
for d in data:
    if 'start' in d:
        s = set(d) - set(['start'])
        start.append(s.pop())
    else:
        conn[d[0]].append(d[1])
        conn[d[1]].append(d[0])
```

```python
conn
```

```python
start
```

```python
s = start[0]
paths = []
path = ''+s
cl = conn[s]
for c in cl:
    if c == 'end':
        paths.append(path)
        break
    elif c.lower() == c and c in path:
        continue
    else:
        path += c
```

```python
paths
```

```python
start
```

```python
conn
```

```python
c = start[0]
paths = []
p = c
while c != 'end':
    for cc in conn[c]:
        if cc.lowercase() not in p:
            p += cc
        c = cc
```

```python
end
```

```python
path = []
for s in start:
    i = s
    path.append(i)
    while i not in end: 
        for j in conn[i]:
            path.append(conn[j])
```

```python
for s in start:
    path.append(s)
    for i in conn[s]:
        path.append(i)
        j = i
        while j not in end:
            for k in conn[j]:
                path.append(k)
                
```

```python

```
