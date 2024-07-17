#############################################
#                                           #
#   Lecture 7 Question 1 : Markov Chain     #
#                                           #
#   Build Markov Chain from given           #
#   transition matrix, compare speed        #
#   with just-in-time compiling   
#                                           #
#   Pietro Rescigno -                       #
#   Scientific Computing with Python 23/24  #
#                                           #
#############################################

# 'Pure - python version'
# [1,0,0] = Bull, [0,1,0] = Bear, [0,0,1] = Stagnant
import numpy as np
import matplotlib.pyplot as plt
from numba import njit
import time
T = np.array([[0.9,0.15,0.25],[0.075,0.8,0.25],[0.025,0.05,0.5]],dtype=np.float64)

Ntot = 90000

def markov_chain(T,Ntot):
    r = np.random.randint(0,2)
    r=0
    if r==0:
        d = np.array([1,0,0],dtype=np.float64)
    elif r==1:
        d = np.array([0,1,0],dtype=np.float64)
    else:
        d = np.array([0,0,1],dtype=np.float64)
    nbull = 0
    nbear = 0
    nstag = 1

    bull_history = []
    bear_history = []
    stag_history = []
    i=1
    #ind = np.arange(1,Ntot+1,1)#,dtype=np.int64)
    #for i in ind:
    while(i<Ntot+1):
        d = np.dot(T,d)
        r = np.random.rand()
        if r<d[0]:
            d = np.array([1,0,0],dtype=np.float64)
            nbull = nbull + 1
        else:
            r = r-d[0]
            if r<d[1]:
                d = np.array([0,1,0],dtype=np.float64)
                nbear = nbear + 1
            else:
                d = np.array([0,0,1],dtype=np.float64)
                nstag = nstag + 1
        bull_history.append(nbull/(i+1))
        bear_history.append(nbear/(i+1))
        stag_history.append(nstag/(i+1))
        i=i+1
    fbull = nbull/Ntot
    fbear = nbear/Ntot
    fstag = nstag/Ntot
    return fbull, fbear, fstag, bull_history, bear_history, stag_history

t0 = time.time() 

for x in range(10):
	fbu,fbe,fst,bu_hist,be_hist,st_hist = markov_chain(T,Ntot)
t = time.time()
print(f'No njit:')
print(f'Fraction of bull days: {fbu:1.4f}')
print(f'Fraction of bear days: {fbe:1.4f}')
print(f'Fraction of stag days: {fst:1.4f}')
print(f'Elapsed time : {(t-t0):1.4f}')
plt.plot(bu_hist,color='blue',label='Bull')
plt.plot(range(Ntot),fbu*np.ones(Ntot),'--',color='blue')
plt.plot(be_hist,color='orange',label='Bear')
plt.plot(range(Ntot),fbe*np.ones(Ntot),'--',color='orange')
plt.plot(st_hist,color='green',label='Stag')
plt.plot(range(Ntot),fst*np.ones(Ntot),'--',color='green')
plt.legend()
plt.show()

# Numba version #

numba_mc = njit(markov_chain)

fbu,fbe,fst,bu_hist,be_hist,st_hist = numba_mc(T,Ntot)

t0 = time.time()
for x in range(10):
	fbu,fbe,fst,bu_hist,be_hist,st_hist = numba_mc(T,Ntot)
t = time.time()
print('\nWith njit :')
print(f'Fraction of bull days: {fbu:1.4f}')
print(f'Fraction of bear days: {fbe:1.4f}')
print(f'Fraction of stag days: {fst:1.4f}')
print(f'Elapsed time : {(t-t0):1.4f}')
plt.plot(bu_hist,color='blue',label='Bull')
plt.plot(range(Ntot),fbu*np.ones(Ntot),'--',color='blue')
plt.plot(be_hist,color='orange',label='Bear')
plt.plot(range(Ntot),fbe*np.ones(Ntot),'--',color='orange')
plt.plot(st_hist,color='green',label='Stag')
plt.plot(range(Ntot),fst*np.ones(Ntot),'--',color='green')
plt.legend()
plt.show()
