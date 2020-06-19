# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import intcode as intcode

df_data = pd.read_csv('inputs/Day15-input.txt',header=None).T

data_org = df_data.values.copy().flatten()

data = np.zeros((10000),dtype=int)
for i in range(len(data_org)):
    data[i] = data_org[i]

space = np.full((1000,1000),9,float)

step={'north':(0,-1),'south':(0,1),'west':(-1,0),'east':(1,0)}
inputs={'north':1,'south':2,'west':3,'east':4}

random.seed(2)
# random.seed(4)

def drone_move(x,y,move='north'):
    inp = inputs[move]
    flag = intcode.Intcode(data,inp=inp)
    step_x,step_y = step[move]
    if flag == 1 or flag == 2:
        y = y+step_y
        x = x+step_x
        space[y,x] = flag
    else:
        space[y+step_y,x+step_x] = flag
    return x,y,flag

x0 = 500
y0 = 500

x = x0
y = y0
space[y,x] = 1

def plot_map(state,xs,ys,fn,curr_pos=None):
    R = sorted([i for (i,j) in state])
    C = sorted([j for (i,j) in state])
    # R = [481,519]
    # C = [479,515]

    with open(fn,'w') as f:
        for r in range(R[0],R[-1]+1):
            for c in range(C[0],C[-1]+1):
                if (r,c) in state:
                    ch = ' '+state[(r,c)]
                else:
                    ch = '  '
                if (r,c) == (500,500):
                    ch = ' O'
                if (r,c) == (xs,ys) and curr_pos is not None:
                    ch = ' D'
                print(ch,end='',file=f)
            print('',file=f)


# + {"jupyter": {"outputs_hidden": true}}
direc = ['north','south','west','east']
status = 9
places = {(x,y):'.'}
cnt = 0
while status!=2:
    i = random.randint(0,3)
    x,y,status = drone_move(x,y,direc[i])
    if (x,y) in places and status!=0:
        continue
    if status == 1:
        print(f'moved {direc[i]} and now at pos: ({x},{y})')
        places[(x,y)] = '.'
    elif status == 0:
        print(f"tried moving {direc[i]}, but hit a wall")
        step_x,step_y = step[direc[i]]
        places[(x+step_x,y+step_y)] = '#'
    else:
        print("Oxygen found at"," x=",x," y=",y)
        places[(x,y)]='X'
    # fn = f'day15_out_{cnt:05d}.dat'
    # plot_map(places,x,y,fn)
    # cnt+=1

plot_map(places,x,y,"plots/Oxygen_map.txt")
# print('max row is ',R[0],R[-1],'max col is ',C[0],C[-1])
