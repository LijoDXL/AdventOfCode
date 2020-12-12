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
with open('inputs/day3.txt') as f:
    lines = f.readlines()
```

```python
lines = [l.strip() for l in lines]
```

```python
def cntTrees(field,right,down,patternLen):
    trees = 0
    if field[0][0] == '#':
        trees+=1
    for i in range(1,len(field)+1-down):
        row = i+down
        if down > 1:
            col = (right*(i+2-1))+1
        else:
            col = (right*(row-1))+1
        if col > patternLen:
            col = col%patternLen
        if field[row-1][col-1] == '#':
            trees+=1
    return trees
```

```python
ex1 = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
ex1 = ex1.split('\n')
ex1_len = len(ex1[0])
```

```python
assert cntTrees(ex1,3,1,len(ex1[0])) == 7
```

## Part 1

```python
cntTrees(lines,3,1,len(lines[0]))
```

## Part 2

```python
cntTrees(ex1,1,2,len(ex1[0]))
```

```python
assert cntTrees(ex1,1,1,len(ex1[0])) == 2
assert cntTrees(ex1,3,1,len(ex1[0])) == 7
assert cntTrees(ex1,5,1,len(ex1[0])) == 3
assert cntTrees(ex1,7,1,len(ex1[0])) == 4
assert cntTrees(ex1,1,2,len(ex1[0])) == 2
```

```python
(c1,c2,c3,c4,c5) = (cntTrees(lines,1,1,len(lines[0])),cntTrees(lines,3,1,len(lines[0])),cntTrees(lines,5,1,len(lines[0])),cntTrees(lines,7,1,len(lines[0])),cntTrees(lines,1,2,len(lines[0])))
```

```python
c1*c2*c3*c4*c5
```

```python

```
