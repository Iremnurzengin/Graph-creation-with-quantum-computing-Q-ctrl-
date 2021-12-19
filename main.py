# tutorial link : https://www.youtube.com/watch?v=wMvUJuwrWqw
# importing packages

from qctrl import Qctrl
import numpy as np
import matplotlib.pyplot as plt
from qctrlvisualizer import get_qctrl_style, plot_controls
plt.style.use(get_qctrl_style())

#start a session with q-ctrl API
qctrl=Qctrl() 
# (we consider a single qubit system represented by hamiltonian, we want to optimize smt to perform a Y gate )

#defining standart metrices
sigma_x= np.array([[0,1], [1,0]])
sigma_y= np.array([[0,1j], [-1j,0]])
sigma_z= np.array([[1,0], [0,-1]])

#defining physical constants and parameters
segment_count= 20 
duration =10e-6 #s
omega_max= 2 * np.pi * 0.5e6 #hz
alpha_max= 2 * np.pi * 0.5e6 #hz
nu = 2 * np.pi * 0.5 * 1e6 # hz

with qctrl.create_graph[] as graph 

#create optimizable pwc controls for omega and sigma
#omega(t) signal 
omega = qctrl.operations.pwc_signal(values=qctrl.operations.optimization_variable(count=segment_count, lower_bound=0, upper_bound=omega_max),duration=duration, name='Ω(t)')

#alpha(t) signal
omega = qctrl.operations.pwc_signal(values=qctrl.operations.optimization_variable(count=segment_count, lower_bound=-alpha_max, upper_bound=alpha_max),duration=duration, name='α(t)')

#Create PWC operators representing each term.
#omega_term = omega * sigma_x
omega_term = qctrl.operations.pwc_operator(signal=omega, operator= sigma_x)

# alpha_term = alpha * sigma_z / 2 
alpha_term = qctrl.operations.pwc_operator(signal=alpha, operator=sigma_z)

#detuning = nu* sigma_z / 2







