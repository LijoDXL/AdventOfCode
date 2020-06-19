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
```

```python
count = 0
for i in range(353096,843212):
    crt_1 = False
    crt_2 = False
    num_arr = np.array([int(j) for j in str(i)])
    diff = num_arr[1:] - num_arr[:-1]
    if (diff==0).sum() > 0:
        crt_1 = True
        if (diff>=0).all():
            crt_2 = True
            count+=1
```

```python
# solution
print("Number of possible passwords:", count)
```

## Part-2

```python
count = 0
for i in range(353096,843212):
    crt_1 = False
    crt_2 = False
    crt_3 = False
    num_arr = np.array([int(j) for j in str(i)])
    diff = num_arr[1:] - num_arr[:-1]
    if (diff==0).sum() > 0:
        crt_1 = True
        if (diff>=0).all():
            crt_2 = True
            fetch_arr = num_arr[1:]
            rep_dig = fetch_arr[diff==0]
            _,cnt = np.unique(rep_dig,return_counts=True)
            if (cnt==1).any():
                crt_3 = True
                count+=1
```

```python
print("Number of possible passwords now will be: ", count)
```

```python

```
