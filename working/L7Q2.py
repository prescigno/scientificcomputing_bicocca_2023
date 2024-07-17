'''
    Lecture 7, Question 2: Decorators

    Here I implement a decorator that sets preferred font size and style
    for plots 
'''
import matplotlib
import matplotlib.pyplot as plt
import scipy
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
def set_fonts(func):
	def wrapper():
		matplotlib.rc('text', usetex=True)
		matplotlib.rc('font', family='serif')
		matplotlib.rcParams.update({'font.size': 10})
		func()
	return wrapper


@set_fonts
def my_plot():
	x=np.arange(0,2*np.pi,2*np.pi/50)
	y=np.sin(x)
	plt.plot(x,y)
	plt.show()

my_plot()	
