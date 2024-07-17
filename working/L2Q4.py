"""
    Lecture 2 Question 4 : Bootstrap

    Pietro Rescigno - Scientific Computing with Python 23/24
"""

import numpy as np
import matplotlib.pyplot as plt
import random

def add_noise(x):
	for i in range(len(x)):
		r=np.random.uniform()
		if r<0.1:
			x[i] = x[i]*3

size = [100] # Size of original sample and bootstrap samples

n_samp = [50, 500, 5000] # Number of bootstrap samples

original = []  # Arrays that will contain the original samples
original_mean = []
original_meanerr = []

# Create bootstrap samples
samples = []
samp_mean = []
fig,ax=plt.subplots()
plt.title("Bootstrap sample mean")
for n in range(len(size)):
	original.append(np.random.normal(1.0,0.5,size[n]))
	add_noise(original[n])
	original_mean.append(np.mean(original[n]))
	original_meanerr.append(np.std(original[n])/np.sqrt(size[n]))
	samples.append([])
	samp_mean.append([])
	print(f"\n---- Sample size: N = {size[n]} ----\n")
	print(f"--------- Original sample: ---------\n")
	print(f"Mean: {original_mean[n]:1.6f}\n")
	print(f"Error on mean :{original_meanerr[n]:1.6f}\n")
	print(f"95% CI : [{(original_mean[n]-2*original_meanerr[n]):1.6f},{(original_mean[n]+2*original_meanerr[n]):1.6f}]\n\n")
	for s in n_samp:
		for i in range(s):
			samples[n].append(np.random.choice(original[n],size=size[n],replace=True))
			samp_mean[n].append(np.mean(samples[n][i]))
		# Compute 95 percentile
		samp_mean[n].sort()
		ql=np.percentile(samp_mean[n],2.5)
		qh=np.percentile(samp_mean[n],97.5)
		print(f"---- S = {s} bootstrap samples -----\n")
		print(f"95% CI : [{ql:1.6f},{qh:1.6f}]\n")
		plt.hist(samp_mean[n],bins=20,density=True,alpha=0.5,label=f'{s} samples',color='C'+str(s%7))
		plt.vlines([ql,qh],0,ax.get_ylim()[1],linestyle='dashed',color='C'+str(s%7))
		ql=np.percentile(samp_mean[n],16.0)
		qh=np.percentile(samp_mean[n],84.0)
		plt.vlines([ql,qh],0,ax.get_ylim()[1],color='C'+str(s%7))

		

#plt.hist(original[0],bins=30,density=True,label=f'Original sample, N={size[0]}')
#plt.vlines(original_mean[0],0,1,color='red',linestyle='dashed')
#ax.axvspan(original_mean[0]-original_meanerr[0],original_mean[0]+original_meanerr[0],color='red',alpha=0.5)
plt.legend()
plt.show()
		
	
