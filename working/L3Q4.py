'''
Lecture 3 question 4:

Usage: python L3Q4.py
produces temperature.pdf

Pietro Rescigno - Scientific computing with python

'''

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.cm import ScalarMappable
matplotlib.rc('text', usetex=True)
matplotlib.rc('font', family='serif')

matplotlib.rcParams.update({'font.size': 10})

y,T,Ts = np.loadtxt('temperature.txt',unpack=True,usecols=(0,1,2))
# Define colormaps normalized to data:
# T: blue for T<0, red for T>0 with intensity proportional to absolute value
norm = matplotlib.colors.Normalize(vmin=min(T),vmax=abs(min(T)))
T_cmap = matplotlib.cm.ScalarMappable(norm=norm, cmap=matplotlib.cm.bwr)

fig,ax=plt.subplots()
# Color each point on a gradient from blue to red based on their temperature
for i in range(len(y)):
	plt.plot(y[i],T[i],'.',color=T_cmap.to_rgba(T[i]))

plt.plot(y,Ts,'-',color='grey',label='5-year smoothing')
plt.xlabel("Year")
plt.ylabel("Temperature anomaly w.r.t 1951-1980 (°C)")
plt.legend()
plt.show()
pdf=PdfPages('temperature.pdf')
pdf.savefig(fig)
pdf.close()




