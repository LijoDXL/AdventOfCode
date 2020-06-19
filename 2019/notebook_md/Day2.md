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
import numpy as np
```

```python
df_data = pd.read_csv('Day2-input.txt',header=None).T
```

```python
data = df_data.values
```

```python
test1 = np.array([1,0,0,0,99])
test2 = np.array([2,3,0,3,99])
test3 = np.array([2,4,4,5,99,0])
test4 = np.array([1,1,1,4,99,5,6,0,99])
```

```python
def intcode(arr):
    a = arr.copy().flatten()
    for n in range(0,len(a),4):
        if a[n] == 99:
            break
        else:
            pos1 = a[n+1]
            pos2 = a[n+2]
            pos3 = a[n+3]
        if a[n] == 1:
            a[pos3] = a[pos1] + a[pos2]
        elif a[n] == 2:
            a[pos3] = a[pos1] * a[pos2]
        else:
            print('unknown opcode')
    return a
```

```python
assert (intcode(test1) == np.array([2,0,0,0,99])).all()
assert (intcode(test2) == np.array([2,3,0,6,99])).all()
assert (intcode(test3) == np.array([2,4,4,5,99,9801])).all()
assert (intcode(test4) == np.array([30,1,1,4,2,5,6,0,99])).all()
```

```python
data[1] = 12
data[2] = 2
```

```python
# value left at position 0 after intcode runs
intcode(data)[0]
```

## Part-2

```python
target = 19690720
```

```python
df_data = pd.read_csv('Day2-input.txt',header=None).T
```

```python
arr_org = df_data.values.copy()
```

```python
for i in range(100):
    flag = 0
    print("now i:",i)
    for j in range(100):
        array = arr_org.copy()
        array[1] = i
        array[2] = j
        if intcode(array)[0] == target:
            print("noun is",i,"and verb is",j)
            flag = 1
            break
    if flag:
        break
```

```python
# solution
print(100*i+j)
```

```python

```
