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
import numpy as np
%matplotlib inline
```

```python
import matplotlib.pyplot as plt
```

```python
image = np.genfromtxt('Day8-input.txt',delimiter=1)
```

```python
image_layer = image.reshape((100,6,25))
```

```python
num = []
for i in range(100):
    lyr = image_layer[i,:,:]
    num.append((lyr==0).sum())
```

```python
idx_min = np.array(num).argmin()
ones = (image_layer[idx_min]==1).sum()
twoes = (image_layer[idx_min]==2).sum()
```

```python
print("product of 1's and 2's:",ones*twoes)
```

## Part-2

```python
arg = np.argmax(image_layer!=2,axis=0)
```

```python
image_arr = np.zeros_like(image_layer[0,:,:])
for r in range(image_arr.shape[0]):
    for c in range(image_arr.shape[1]):
        image_arr[r,c] = image_layer[arg[r,c],r,c]
```

```python
plt.imshow(image_arr)
```

```python

```
