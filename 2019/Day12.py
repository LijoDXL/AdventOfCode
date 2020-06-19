import numpy as np
import matplotlib.pyplot as plt
import sys

pos0_inp = np.array([[-4,-9,-3],[-13,-11,0],[-17,-7,15],[-16,4,2]])
vel0_inp = np.array([[0,0,0],[0,0,0],[0,0,0],[0,0,0]])

pos0_test1 = np.array([[-1,0,2],[2,-10,-7],[4,-8,8],[3,5,-1]])
vel0_test1 = np.zeros_like(pos0_test1)

pos0_test2 = np.array([[-8,-10,0],[5,5,10],[2,-7,3],[9,-8,-3]])
vel0_test2 = np.zeros_like(pos0_test2)

def update(pos,vel):
    vel_ = []
    for i in range(4):
        dv = np.where(pos[i] > pos,-1,-999)
        dv = np.where(pos[i] < pos,1,dv)
        dv = np.where(pos[i] == pos,0,dv)
        vel_.append(dv.sum(axis=0))
    vel_n = np.vstack(vel_) + vel
    pos_n = pos+vel_n
    return pos_n,vel_n

def energy(tsteps,p_in,v_in):
    p = p_in.copy()
    v = v_in.copy()
    for t in range(1,tsteps+1):
        p,v = update(p,v)
    return (np.abs(p).sum(axis=1) * np.abs(v).sum(axis=1)).sum()


assert energy(10,pos0_test1,vel0_test1)==179,"test 1 for energy fail"

assert energy(100,pos0_test2,vel0_test2)==1940,"test 2 for energy fail"

# solution
print("The energy required is: ",energy(1000,pos0_inp,vel0_inp))


# ## Part-2

def repeat_check(pos,vel,n=5):
    """Find number of iterations needed to repeat velocity and position
    Parameter:
    ===========
        pos : numpy array
            initial position of the moons
        vel : numpy array
            initial velocity of the moons
        n : int
            number of repeats; checks the consistency of repeat pattern
            for example n=5 implies check if repetition remains same for 5 times
    Return:
    ========
        ans : int
              iteration number for which the pos and vel state repeats
    """
    p = pos.copy()
    v = vel.copy()
    freq = []
    for i in range(3):
        print("Finding match for axis ",i)
        print("="*30)
        cnt = 0
        p_cnt = 0
        repeat_frq_list = []
        while True:
            p,v = update(p,v)
            cnt+=1
            v_flag = (v[:,i] == vel[:,i]).all()
            if v_flag:
                p_flag = (p[:,i] == pos[:,i]).all()
                if p_flag:
                    # print("   Match found in iteration #",cnt)
                    # print("position;\n",p,"\nvelocity;\n",v)
                    repeat_frq_list.append(cnt)
                    p_cnt+=1
                    if p_cnt == n:
                        break
        if (np.diff(repeat_frq_list,n=2)==0).all():
            freq.append(repeat_frq_list[1]-repeat_frq_list[0])
        else:
            print("Inconsistency in freq for axis ",i)
    if len(freq) == 3:
        ans = np.lcm(np.lcm(freq[0],freq[1]),freq[2])
        return ans
    else:
        return 0

assert repeat_check(pos0_test1,vel0_test1,5)==2772,"test 1 fail"
assert repeat_check(pos0_test2,vel0_test2,5)==4686774924,"test 2 fail"

ans = repeat_check(pos0_inp,vel0_inp,5)
if ans != 0:
    print("The universe repeats itself after ",ans,"iterations")
else:
    print("Something is wrong")
