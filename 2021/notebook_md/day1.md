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
import pandas as pd
```

```python
def getData(fpath,**kwargs):
    return pd.read_csv(fpath,header=None,**kwargs)
```

## Part-1

```python
dfex1 =  getData('input/day1ex1.txt',names=['depth'])
df =  getData('input/day1.txt',names=['depth'])
```

```python
# count increasing depths
cnt = (dfex1.diff()>0).sum().values[0]
```

```python
assert cnt == 7,"WRONG!"
```

```python
# count increasing depths
cnt = (df.diff()>0).sum().values[0]
```

```python
print("the number of increasing values are:",cnt)
```

### Part-2

```python
# count in groups of 3 and check if increasing
cnt = (dfex1.rolling(3).sum().diff()>0).sum().values[0]
```

```python
assert cnt == 5,"WRONG!"
```

```python
# count in groups of 3 and check if increasing
cnt = (df.rolling(3).sum().diff()>0).sum().values[0]
```

```python
print("the number of increasing values are:",cnt)
```

```python

```
