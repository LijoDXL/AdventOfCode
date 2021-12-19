def step(x,y,u,v):
    x += u
    y += v

    g = -1
    if u > 0:
        d = -1
    elif u ==0:
        d = 0
    else:
        d = 1

    u += d
    v += g
    return x,y,u,v

# target = [20,30,-10,-5] # xmin,xmax,ymin,ymax
target = [244,303,-91,-54] # xmin,xmax,ymin,ymax
x0 = 0
y0 = 0

min_max_u = []
togg = False
for i in range(1,2000):
    t = 0
    u0 = i
    v0 = 3
    x = x0
    y = y0
    u = u0
    v = v0
    flag = False
    while True:
        t += 1
        x,y,u,v = step(x,y,u,v)
        if target[0]<=x<=target[1]:
            flag = True
            break
        elif x > target[1]:
            break
        elif u == 0:
            break
    if togg != flag:
        min_max_u.append(u0)
        togg = flag
    if flag:
        print(f"******valid x vel is:{u0}*****")
    else:
        print(f"[==={u0} is not valid=====]")
valid_u = [min_max_u[0],min_max_u[1]-1]
valid_v = [1,abs(target[2])-1] # -9-1 = -10

# Explanation for valid_v:
#==========================#
# time it takes to reach top (T) is when v=0;
# vf = vi+at => 0 = vi-T => vi = T  --(1)
# time it takes to reach y=0 will  be 2T;
# when at top for 1 time step y remains same as previous,
# so time step when y=0 will be 2T+1;
# v at 2T+1 will be (vf=vi+at=>vf=vi-(2T+1)=>vf=vi-2vi-1)
# hence v at 2T+1 is -vi-1. If this v is greater than -10, it will overshoot traget

###Part-1
y_dis = []
for i in range(valid_u[0],valid_u[1]+1):
    for j in range(valid_v[0],valid_v[1]+1):
        x = 0
        y = 0
        u = i
        v = j
        y_max = 0
        flag = False
        while True:
            x,y,u,v = step(x,y,u,v)
            if y > y_max:
                y_max = y
            if target[0]<=x<=target[1] and target[2]<=y<=target[3]:
                flag = True
                break
            elif x > target[1] or y < target[2]:
                break
        if flag:
            y_dis.append(y_max)
ans = max(y_dis)
print(ans)

##Part-2
cnt = 0
for i in range(0,500):
    for j in range(-100,100):
        x = 0
        y = 0
        u = i
        v = j
        while True:
            x,y,u,v = step(x,y,u,v)
            if target[0]<=x<=target[1] and target[2]<=y<=target[3]:
                cnt += 1
                break
            elif x > target[1] or y < target[2]:
                break
print(cnt)
