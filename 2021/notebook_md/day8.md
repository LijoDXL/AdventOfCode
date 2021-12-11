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
from collections import defaultdict
```

```python
with open('input/day8.txt') as f:
    data = [f.strip() for f in f.readlines()]
```

```python
fdigits = [x.split(' | ')[1] for x in data]
```

```python
count = 0
for i in fdigits:
    for j in i.split():
        if len(j) in [2,4,3,7]:
            count += 1
```

```python
#assert count == 26,"WRONG!"
```

```python
print("The answer is",count)
```

### Part 2

```python
def match(search,item):
    """Find the element from the search list with maximum match with item
    Params:
    ========
        search: List of str
                list of searchable items
        item:  str
               element to be matched
    Returns:
    ==========
        str,element with the most match        
    """
    for i in search:
        cnt = 0
        for j in [x for x in item]:
            if j in [x for x in i]:
                cnt += 1
        if cnt == 5:
            return i
```

```python
def printNum(digit,decoder):
    """Find digit by decoding to original segment and print it.
    Params:
    =========
        digit  : str
                 encoded digit
        decoder: dict
                 mapping to original segment
    Returns:
    ==========
        str, decoded digit
    """
    numDict = {0: 'a,b,c,e,f,g',
                1: 'c,f',
                2: 'a,c,d,e,g',
                3: 'a,c,d,f,g',
                4: 'b,c,d,f',
                5: 'a,b,d,f,g',      
                6: 'a,b,d,e,f,g',
                7: 'a,c,f',
                8: 'a,b,c,d,e,f,g',
                9: 'a,b,c,d,f,g'}
    num = ''
    for i in digit:
        num += decoder[i]
    for k,v in numDict.items():
        if v.split(',') == sorted(num):
            return str(k)
    return None
```

```python
def getDigits(line):
    #line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    data,digits = line.strip().split(' | ')
    myseg = defaultdict(list)  # dict to access segments by its length
    for d in data.split():
        myseg[len(d)].append(d)
    for i in [2,4,3,7]:   # single element list as just elements
        myseg[i] = myseg[i][0]
    pairs = {} # store deductions
    for i in myseg[3]:
        if i not in myseg[2]: # compare digit 7 and 1
            pairs['a'] = i
    pairs['cf'] = myseg[2]
    pairs['bd'] = '' # get next pair from digit 4
    for i in myseg[4]: 
        if i not in myseg[2]:
            pairs['bd'] += i
    pairs['eg'] = '' # get next pair from digit 8
    for i in myseg[7]:
        if i not in ''.join(pairs.values()):
            pairs['eg'] += i
    
    ms = pairs['a']+pairs['cf']+pairs['eg'] # get b from digit 0
    matched = match(myseg[6],ms)
    pairs['b'] = [x for x in matched if x not in ms][0]
    
    ms = pairs['a']+pairs['bd']+pairs['eg'] # get f from digit 6
    matched = match(myseg[6],ms)
    pairs['f'] = [x for x in matched if x not in ms][0]
    
    ms = pairs['a']+pairs['bd']+pairs['cf'] # get g from digit 9
    matched = match(myseg[6],ms)
    pairs['g'] = [x for x in matched if x not in ms][0]
    
    # use the pairs found so far for rest of the  characters
    pairs['c'] = [x for x in pairs['cf'] if x not in pairs['f']][0]
    pairs['e'] = [x for x in pairs['eg'] if x not in pairs['g']][0]
    pairs['d'] = [x for x in pairs['bd'] if x not in pairs['b']][0]
    
    decode = {} # decoder mapping
    for k in pairs.keys():
        if len(k) == 1:
            decode[pairs[k]] = k
    
    fourDigit = ''
    for d in digits.split():
        fourDigit += printNum(d,decode)
    return fourDigit
```

```python
#line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
#getDigits(line)
#data,digits = line.strip().split(' | ')
```

```python
digits = [getDigits(line)for line in data]
```

```python
#assert sum(map(int,digits)) == 61229,"WRONG!"
```

```python
print("The sum is:",sum(map(int,digits)))
```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

orgseg = {2:'cf',3:'acf',4:'bcdf',7:'abcdefg',6:['abcefg','abdefg','abcdfg'],5:['acdeg','acdfg','abdfg']}

0: a,b,c,e,f,g    cfbdeg
1: c,f
2: a,c,d,e,g      
3: a,c,d,f,g 
4: b,c,d,f
5: a,b,d,f,g      
6: a,b,d,e,f,g     cfabd[_]
7: a,c,f
8: a,b,c,d,e,f,g
9: a,b,c,d,f,g    cfaeg[]

cefabd cdfgeb  cagedb 

0: 6
*1: 2
2: 5
3: 5
*4: 4
5: 5
6: 6
*7: 3
*8: 7
9: 6

  8:   
 aaaa  
b    c     a:c , [d:a], e:b, f:d, g:e, b:f, c:g
b    c
 dddd 
e    f
e    f
 gggg    


acedgfb, ab  , eafb , dab 
ab --> 1 --> cf, [fc]
dab --> 7 --> acf             {comfirm ab:[cf], d:a}
eafb --> 4 --> bcdf       {confirm ef:bd}
acedgfb --> 8 -->         {confirm cg --> eg}




```python

```
