import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

################ This defines the differential equation data ( need to llok at manual for odeint in scipy

def differential(y,t):
     pos=y[0]
     vel= y[1]
     out= [vel, -pos**3]
     return out

def freq(s):
    angdat=np.array(s[:,0])
    fourier=np.fft.fft(angdat)
    Power= abs(fourier**2)
    freq= np.argmax(Power[0:int(ttot/(2*deltat))])
    frq_true= freq/ttot
    return frq_true   
    
pos_0 = 0
vel_0 = 0
ini=[pos_0, vel_0]

deltat= 0.01
ttot=100

t=np.linspace(0,ttot, int(ttot/deltat))
amplitudes = []
frequencies = []
for x in range(1,101,5):
    amplitudes.append(x)
    ini[0] = x
    solution=odeint(differential, ini, t)
    frequencies.append(freq(solution))
    print(x)

slope, intercept = np.polyfit(np.log(amplitudes), np.log(frequencies), 1)
print("The slope/scaling is", slope)
plt.xlabel("Amplitude")
plt.ylabel("Frequency")
plt.loglog(amplitudes, frequencies, label = "Scaling factor " + str(slope))
plt.legend(loc = 'best')
plt.show()