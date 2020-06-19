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
%matplotlib inline
```

```python
df = pd.read_csv('Day6-input.txt',header=None,sep=')',names=['L','R'])
```

```python
df_test = pd.read_csv('Day6-TestInput.txt',header=None,sep=')',names=['L','R'])
df_test2 = pd.read_csv('Day6-TestInput2.txt',header=None,sep=')',names=['L','R'])
```

```python
#count = np.zeros((len(df_test)),dtype=int)
count = 0
for i in df['R']:
    assert len(df.loc[df['R']==i,'L'].values),1
    orbit_arnd = df.loc[df['R']==i,'L'].values[0]
    count+=1
    #print(orbit_arnd)
    while orbit_arnd != 'COM':
        orbit_arnd = df.loc[df['R']==orbit_arnd,'L'].values[0]
        count+=1
        #print(orbit_arnd)
```

```python
print("Total direct and indirect orbits:",count)
```

## Part-2

```python
san_path = df.loc[df['R']=='SAN','L'].values[0]
you_path = df.loc[df['R']=='YOU','L'].values[0]
flag = 0
s_count = 0
y_count = 0
count = s_count+y_count
while san_path != 'COM':
    you_path = df.loc[df['R']=='YOU','L'].values[0]
    y_count = 0
    #print("san_path:",san_path)
    while you_path != 'COM':
        #print("you_path:",you_path)
        if san_path == you_path:
            print("I am in")
            flag = 1
            break
        you_path = df.loc[df['R']==you_path,'L'].values[0]
        y_count+=1
    if flag:
        break
    san_path = df.loc[df['R']==san_path,'L'].values[0]
    s_count+=1
count = s_count+y_count
#print(s_count,y_count)
print("number of orbit transfer required:",count)
```

```python

```
