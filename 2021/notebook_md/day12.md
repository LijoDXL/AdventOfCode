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
with open('input/day12ex1.txt') as f:
    data = [d.strip().split('-') for d in f.readlines()]
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
paths = []
path = ''
for s in start:
    P = conn[s]
    while P:
        c = P.pop()
        path+=s
        if c == 'end':
            paths.append(path)
            path = ''
            continue
        elif c.lower() == c:
            if c not in path:
                path += c
        else:
            path += c
        for i in conn[c]:
            P.append(i)
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

```
