with open('input/day16ex.txt') as f:
    data = [d.strip() for d in f.readlines()]
IN = data[0]
BIN = bin(int(IN,16))[2:]

def parseP(P,i0=0):
    i1 = i0 + 3
    ver = int('0'+P[i0:i1],2)
    i0 = i1
    i1 = i0+3
    typ = int('0'+P[i0:i1],2)
    i0 = i1
    return (ver,typ),i0

def parsePnew(P,i0=0):
    i1 = i0 + 1
    ltype = P[i1]
    i0 = i1
    if lytpe == '0':
        i1 = i0 + 15
        tot_len = int(P[i0:i1],2)
        i0 = i1
        (v,t),i0 = parseP(P,i0)
        if t == 4:
            lnums,i0 = literalC(P,i0)
            return lnums,i0
        else:
            while cnt <= tot_len:
                i0 = parsePnew(P,i0)


    i1 = i0+3
    typ = int('0'+P[i0:i1],2)
    i0 = i1
    return (ver,typ),i0

def literalC(P,i0):
    i1 = i0+5
    E = P[i0:i1]
    e = E[0]
    lnum = []
    while e != '0':
        bnum = E[1:5]
        lnum.append(bnum)
        i0 = i1
        i1 = i0+5
        E = P[i0:i1]
        e = E[0]
    lnum.append(E[1:5])
    return lnum,i1

(v,t),pos = parseP(BIN)

if t == 4:
    lnums,pos = literalC(BIN,pos)
else:

