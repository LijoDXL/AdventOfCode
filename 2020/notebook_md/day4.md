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
record = []
data = []
with open('inputs/day4.txt','r') as f:
    for line in f:
        l = line.strip()
        if not l:
            record.append(data)
            data = []
        else:
            data.append(l)
record.append(data)
```

```python
rec_dict = [{i.split(':')[0]:i.split(':')[1] for i in ' '.join(rc).split()} for rc in record]
```

```python
def checkValid(data_dict,cid_flag=1):
    valid = 0
    for r in data_dict:
        if len(r.keys()) == 8:
            valid+=1
        if len(r.keys()) == 7:
            if cid_flag:
                if 'cid' not in r:
                    valid+=1
    return valid
```

```python
checkValid(rec_dict)
```

## Part 2

```python
def checkValidity(r):
    
    byr_flg = (len(r['byr']) == 4 and int(r['byr']) >= 1920 and int(r['byr']) <= 2002)
    iyr_flg = (len(r['iyr']) == 4 and int(r['iyr']) >= 2010 and int(r['iyr']) <= 2020)
    eyr_flg = (len(r['eyr']) == 4 and int(r['eyr']) >= 2020 and int(r['eyr']) <= 2030)
    ecl_flg = r['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']
    pid_flg = (len(r['pid'])==9 and r['pid'].isdigit())
    def hgtCheck(r):
        unit = r['hgt'][-2:]
        if unit == 'cm':
            flg = (int(r['hgt'][:-2]) >= 150 and int(r['hgt'][:-2]) <= 193)
        elif unit == 'in':
            flg = (int(r['hgt'][:-2]) >= 59 and int(r['hgt'][:-2]) <= 76)
        else:
            flg = False
        return flg
    def hclCheck(r):
        flg1 = (r['hcl'][0] == '#' and len(r['hcl'][1:])==6)
        flg2 = (sum([i in '0123456789abcdef' for i in r['hcl']]) == 6)
        return flg1 and flg2
    hgt_flg = hgtCheck(r)
    hcl_flg = hclCheck(r)
    
    return (byr_flg and iyr_flg and eyr_flg and ecl_flg and pid_flg and hgt_flg and hcl_flg)
    #return (byr_flg,iyr_flg,eyr_flg,ecl_flg,pid_flg,hgt_flg,hcl_flg)


```

```python
def checkValid2(data_dict,cid_flag=1):
    valid = 0
    for r in data_dict:
        if len(r.keys()) == 8:
            if checkValidity(r):
                valid+=1
        if len(r.keys()) == 7:
            if cid_flag:
                if 'cid' not in r:
                    if checkValidity(r):
                        valid+=1
    return valid
```

<!-- #region -->
```python
# check
ex2 = {i.split(':')[0]:i.split(':')[1] for i in  "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719".split()}
ex2 = [ex2]
tmp = checkValidity(ex2[0])
```
<!-- #endregion -->

```python
checkValid2(rec_dict)
```
