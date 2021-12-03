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

### Part-1

```python
with open('input/day3ex1.txt') as f:
    data = f.readlines()
```

```python
data = [l.rstrip() for l in data]
```

```python
n = len(data[0])
tot = len(data)
```

```python
gamma = []
for i in range(n):
    cnt = [l[i] for l in data].count('1')
    if cnt > tot/2:
        gamma.append('1')
    else:
        gamma.append('0')
```

```python
epsilon = ['1' if l == '0' else '0' for l in gamma]
```

```python
g = int("".join(gamma),2)
```

```python
e = int("".join(epsilon),2)
```

```python
print(g*e)
```

```python
#assert (g*e) == 198,"WRONG!"
```

### Part-2

```python
with open('input/day3.txt') as f:
    data = f.readlines()
data = [l.rstrip() for l in data]
```

```python
def calc(data,rating='O2'):
    n = len(data[0])
    tot = len(data)
    for i in range(n):
        cnt1 = [l[i] for l in data].count('1')
        if rating == 'O2':
            num = '1'
            num_ = '0'
        else:
            num = '0'
            num_ = '1'
        if cnt1 > tot/2:
            data = [l for l in data if l[i] == num ]
        elif cnt1 < tot/2:
            data = [l for l in data if l[i] == num_ ]
        else:
            data = [l for l in data if l[i] == num ]
        tot = len(data)
        if tot == 1:
            print('only one item remains, breaking!')
            break
    return data
```

```python
oxy_r = calc(data,'O2')
co2_r = calc(data,'CO2')
```

```python
r1 = int("".join(oxy_r),2)
r2 = int("".join(co2_r),2)
```

```python
#assert r1*r2 == 230,"WRONG!"
```

```python
print(r1*r2)
```

```python

```
