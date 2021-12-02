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
def calc(fpath):
    xdir = 0
    ydir = 0
    with open(fpath) as f:
        for line in f:
            inst,n = line.split(' ')
            if inst == "forward":
                xdir+=int(n)
            elif inst == "down":
                ydir+=int(n)
            elif inst == "up":
                ydir-=int(n)
            else:
                raise ValueError(f"Unknown instruction {inst}")
    return xdir*ydir
```

```python
assert calc("input/day2ex1.txt") == 150,'WRONG!'
```

```python
calc("input/day2.txt")
```

### Part-2

```python
def calcMod(fpath):
    xdir = 0
    ydir = 0
    aim = 0
    with open(fpath) as f:
        for line in f:
            inst,n = line.split(' ')
            if inst == "forward":
                xdir+=int(n)
                ydir+=(aim*int(n))
            elif inst == "down":
                aim+=int(n)
            elif inst == "up":
                aim-=int(n)
            else:
                raise ValueError(f"Unknown instruction {inst}")
    return xdir*ydir
```

```python
assert calcMod("input/day2ex1.txt") == 900,"WRONG!"
```

```python
calcMod("input/day2.txt")
```

```python

```
