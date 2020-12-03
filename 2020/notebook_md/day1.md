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
import numpy as np
```

```python
data = np.genfromtxt('inputs/day1.txt',dtype=int)
```

```python
dataDiff = 2020-data
intersect = np.intersect1d(dataDiff,data)
print("product is: ",intersect[0]*intersect[1])
```

## Part-2

```python
for i in range(len(data)):
    for j in range(i,len(data)):
        for k in range(j,len(data)):
            tot = data[i]+data[j]+data[k]
            if tot == 2020:
                print("the three numbers are at: ",i,j,k)
                break
        if tot == 2020:
            break
    if tot == 2020:
        break
```

```python
print("the product is: ",data[i]*data[j]*data[k])
```

```python

```
