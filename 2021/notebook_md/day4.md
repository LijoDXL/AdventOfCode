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
def getData(fname):
    with open(f'input/{fname}') as f:
        lines = f.readlines()
        data = [l.strip() for l in lines]
        numbers = data[0].split(',')
    cards = []
    card = []
    for l in data[1:]:
        if l == '':
            if card:
                cards.append(card)
            card = []
        else:
            card.append(l.split())
    cards.append(card)
    return numbers,cards
```

### Part-1

```python
numbers,cards = getData('day4.txt')
```

```python
r = 5
c = 5
win = False
nn = 0
while not win:
    n = numbers[nn]
    for ii,card in enumerate(cards):
        for i in range(r):
            for j in range(c):
                if card[i][j] == n:
                    card[i][j] = True
        # row check
        for i in range(r):
            row = card[i]
            if  row.count(True) == 5:
                print(f"winner is card {ii}")
                win = True
                break
        if win:
            break
        # col check
        for i in range(c):
            col = [k[i] for k in card]
            if  col.count(True) == 5:
                print(f"winner is card {ii}")
                win = True
                break
    nn+=1
```

```python
unmarked_sum = sum([int(i) for j in cards[ii] for i in j if i != True])
print("The score is:",int(n)*unmarked_sum)
```

```python
#assert int(n)*unmarked_sum == 4512, "WRONg!"
```

### Part-2

```python
numbers,cards = getData('day4.txt')
```

```python
r = 5
c = 5
winners = []
over = False
for n in numbers:
    for ii,card in enumerate(cards):
        if ii in winners:
            continue
        for i in range(r):
            for j in range(c):
                if card[i][j] == n:
                    card[i][j] = True
        # row check
        for i in range(r):
            row = card[i]
            if  row.count(True) == 5:
                winners.append(ii)
                print(f"winner found: {ii}")

        # col check
        for i in range(c):
            col = [k[i] for k in card]
            if  col.count(True) == 5:
                if ii not in winners: # prevent double counting of winners
                    winners.append(ii)
                    print(f"winner found: {ii}")
        if len(winners) == len(cards):
            over = True
            break
    if over:
        break
```

```python
unmarked_sum = sum([int(i) for j in cards[ii] for i in j if i != True])
print("The score is:",int(n)*unmarked_sum)
```

```python
#assert int(n)*unmarked_sum == 1924, "WRONg!"
```
