"""
    Lecture 2 question 7 + Lec 3 Q 8: Conway's game of life

    Implements the rules to Conway's game of life and shows the evolution
    for a set of initial conditions.
    	
    Pietro Rescigno - Scientific Computing with Python 23/24
"""

import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import sys

def live_neighbors(grid,i,j,N):
    s=0.
    s+=grid[(i+1)%N][j] # s
    s+=grid[(i+1)%N][(j+1)%N] #se
    s+=grid[(i+1)%N][(j-1)%N] #sw
    s+=grid[i][(j-1)%N] #w
    s+=grid[i][(j+1)%N] #e
    s+=grid[(i-1)%N][(j-1)%N] #nw
    s+=grid[(i-1)%N][j] # n
    s+=grid[(i-1)%N][(j+1)%N] #ne
    return s

def dead_neighbors(grid,i,j,N):
    s=0.
    s+=grid[i+1][j] -1 # s
    s+=grid[i+1][j+1] -1 #se
    s+=grid[i+1][j-1] -1 #sw
    s+=grid[i][j-1] -1 #w
    s+=grid[i][j+1] -1 #e
    s+=grid[i-1][j-1] -1 #nw
    s+=grid[i-1][j] -1 # n
    s+=grid[i-1][j+1] -1 #ne
    return abs(s)

flag=-1
while True:
	flag=input(f"Choose the initial condition:\nglider (0)\npulsar (1):\n")
	flag=int(flag)
	if (flag==0 or flag==1):
		break

N = 15 # grid size
niter = 57 # number of iterations

gridlist = [np.zeros([N,N], dtype=int) for _ in range(niter)]

grid = gridlist[0]


if flag==0:
	grid[10,10]=1
	grid[10,11]=1
	grid[11,9]=1
	grid[11,11]=1
	grid[12,11]=1
	delay=50
else:
	grid[5,2]=1
	grid[8,2]=1
	grid[5,3]=1
	grid[8,3]=1
	grid[4,4]=1
	grid[5,4]=1
	grid[4,5]=1
	grid[8,4]=1
	grid[9,4]=1
	grid[2,5]=1
	grid[3,5]=1
	grid[5,9]=1
	grid[5,10]=1
	grid[9,5]=1
	grid[10,5]=1
	grid[11,5]=1
	
	grid[5,11]=1
	grid[8,11]=1
	grid[5,11]=1
	grid[8,10]=1
	grid[4,9]=1
	grid[4,8]=1
	grid[8,9]=1
	grid[9,9]=1
	grid[2,8]=1
	grid[3,8]=1
	grid[4,8]=1
	grid[9,8]=1
	grid[10,8]=1
	grid[11,8]=1
	
	delay = 333

fig = plt.figure(figsize=(8,8))

im = plt.imshow(grid)

def animate_func(i):
    im.set_array(gridlist[i])
    return [im]

t0=time.time()
for n in range(niter-1):
    grid = gridlist[n]
    nextgrid = gridlist[n+1]
    for i in range(N):
        for j in range(N):
            isalive = grid[i][j]
            L = live_neighbors(grid,i,j,N)
            if isalive:
                if (L< 2 or L>3):
                    nextgrid[i][j]=0
                else:
                    nextgrid[i][j]=grid[i][j]
            else :
                if (L==3):
                    nextgrid[i][j]=1

t1=time.time()
print(f'Built sequence in: {(t1-t0):1.2f}')

anim = animation.FuncAnimation(fig,animate_func,frames=range(niter),interval=delay,blit=True)

plt.show()
