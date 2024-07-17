'''
    Lecture 4 Question 5 : Planetary orbits
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy

def rhs(t,x):
	xdot = x[2]
	ydot = x[3]
	vxdot = - 4*np.pi**2*x[0]/(np.sqrt(x[0]**2+x[1]**2)**3)
	vydot = - 4*np.pi**2*x[1]/(np.sqrt(x[0]**2+x[1]**2)**3)

	return np.array([xdot,ydot,vxdot,vydot])

def ode_integrate(X0,dt,tmax):
	r = scipy.integrate.solve_ivp(rhs, (0., tmax), X0, method="RK45", dense_output=True,rtol=1e-6,atol=1e-9)
	
	ts = np.arange(0.,tmax,dt)
	Xs=r.sol(ts)
	return ts, Xs

a = 1.0 # semi major axis
e = 0.8 # eccentricity

r_peri = a*(1-e)
v_peri = np.sqrt(4*np.pi**2*(1+e)/r_peri) 

x0 = r_peri
y0 = 0.
vx0 = 0.
vy0 = v_peri

X0 = [x0,y0,vx0,vy0]

tmax =5
dt = 1e-3
t,x = ode_integrate(X0,dt,tmax)
print(x.shape)
plt.axes().set_aspect('equal')
plt.plot(x[0][:],x[1][:],'.',markersize=1)
plt.xlabel('x')
plt.ylabel('y')

plt.show()
