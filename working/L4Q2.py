'''
    Lecture 4 question 2: Interpolation error

    Sample a complicated function, build interpolations and compare 
    the accuracy
'''
import scipy
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interpolate
def myfunction(x):
	return np.cos(10*x)*(np.arctan(100*x))*2/np.pi*(np.cos(1.0*x)+np.cos(1.2*(x-0.5))+np.sin(1.3*(x+0.2))+np.sin(1.1*(x-0.3)))

xfine = np.linspace(-5,5,1000000)

line_err=[]
quad_err=[]
cube_err=[]
for N in range(30,6000,100):
	xsamp = np.linspace(-5,5,N)
	fsamp = myfunction(xsamp)

	f_interp_cube=interpolate.interp1d(xsamp,fsamp,kind='cubic')
	f_interp_quad=interpolate.interp1d(xsamp,fsamp,kind='quadratic')
	f_interp_line=interpolate.interp1d(xsamp,fsamp,kind='slinear')

	line_err.append(np.sum(abs(f_interp_line(xfine)-myfunction(xfine))))
	quad_err.append(np.sum(abs(f_interp_quad(xfine)-myfunction(xfine))))
	cube_err.append(np.sum(abs(f_interp_cube(xfine)-myfunction(xfine))))
print('Built errors')
N=30
xsamp = np.linspace(-5,5,N)
fsamp = myfunction(xsamp)

f_interp_cube=interpolate.interp1d(xsamp,fsamp,kind='cubic')
f_interp_quad=interpolate.interp1d(xsamp,fsamp,kind='quadratic')
f_interp_line=interpolate.interp1d(xsamp,fsamp,kind='slinear')

plt.plot(xfine,myfunction(xfine),'--', lw=1,label='True')
plt.plot(xsamp,fsamp,'.',color='red',markersize=4,label='30 Samples') 

#f_interp_cubspline
plt.plot(xfine,f_interp_cube(xfine),'-',lw=1,label='Cubic')
plt.plot(xfine,f_interp_quad(xfine),'-',lw=1,label='Quadratic')
plt.plot(xfine,f_interp_line(xfine),'-',lw=1,label='Linear')
plt.legend()
plt.show() 
plt.clf()
plt.plot(range(30,6000,100),line_err,'.',label='Line')
plt.plot(range(30,6000,100),quad_err,'.',label='Quad')
plt.plot(range(30,6000,100),cube_err,'.',label='Cube')
plt.yscale("log")
plt.xscale("log")
plt.xlabel("Number of nodes")
plt.ylabel("$|| f_{\\rm interp } - f_{\\rm true}||_1$")
plt.legend()
plt.show()
