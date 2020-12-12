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
with open('inputs/day2.txt','r') as f:
    valid_pwd = 0
    for line in f:
        cond,pwd = line.split(':')
        min_max, reqLetter = cond.split(' ')
        mini = int(min_max.split('-')[0])
        maxi = int(min_max.split('-')[1])
        pwd = pwd.strip()
        cnt = pwd.count(reqLetter)
        if cnt <= maxi and cnt >= mini:
            valid_pwd+=1
```

```python
print("Number of valid passowrds are:",valid_pwd)
```

## Part 2

```python
with open('inputs/day2.txt','r') as f:
    valid_pwd = 0
    for line in f:
        cond,pwd = line.split(':')
        pos1_pos2, reqLetter = cond.split(' ')
        pos1 = int(pos1_pos2.split('-')[0])-1
        pos2 = int(pos1_pos2.split('-')[1])-1
        pwd = pwd.strip()
        flg1 = pwd[pos1] == reqLetter
        flg2 = pwd[pos2] == reqLetter
        tot = flg1+flg2
        if tot == 1:
            valid_pwd+=1
```

```python
print("Number of valid passowrds are:",valid_pwd)
```

```python

```
