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
```

```python
def fuel(m):
    return (m//3)-2
```

```python
assert fuel(12)==2
assert fuel(14)==2
assert fuel(1969)==654
assert fuel(100756)==33583
```

```python
df_mass = pd.read_csv('Day1-input.txt',header=None,names=['mass'])
```

```python
# total fuel required
df_mass.transform(fuel).sum()
```

## Part-2

```python
df_fuel = df_mass.transform(fuel)
df_fuel.columns = ['fuel']
df_fuel.head()
```

```python
def additional_fuel(m):
    mass = m
    total = 0
    while mass>=0:
        total+=mass
        mass=(mass//3)-2
    return total
```

```python
assert additional_fuel(fuel(14))==2
assert additional_fuel(fuel(1969))==966
assert additional_fuel(fuel(100756))==50346
```

```python
# fuel required accounting for mass of fuel as well
df_fuel['fuel'].transform(additional_fuel).sum()
```

```python

```
