import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
################# This program tries to solve the differnetial equation x"(t)=-x(t) by finite differences. It uses the leapfrog algorithm (velocities are coputed at half steps to evolve)

def input_float(mes):
    while True:
        try:
            u=float(input(mes))
            return(u)
        except:
            print("You need to input a float")




def exit_seq():
    mes=input("Do you want to continue? y/n ")
    if mes!='y':
        exit()
##################### Read initial conditions

while True:
 
 x0=input_float("Enter the initial postion x-coordinate ")
 y0=input_float("Enter the initial postion y-coordinate ")
 vx0=input_float("enter the initial velocity x ")
 vy0=input_float("enter the initial velocity y ")
 delta_t= input_float("enter the time step ")
 nsteps= int(input_float("Total run time? ")/delta_t)

 labels = "x0 = " + str(x0) + ", \ny0 = " + str(y0) + ", \nvx0 = " + str(vx0) + ", \nvy0 = " + str(vy0) + ", \ntime step = " + str(delta_t) + ", \nn-steps = " + str(nsteps)

 t0=0
 

 x,y,vx,vy,t=[x0],[y0],[vx0],[vy0],[t0]
 momentum = []
 energy = []
 m = (x0*vy0)-(y0*vx0)
 e = ((0.5*(vx0**2)+0.5*(vy0**2))-(1/np.sqrt((abs((x0**2)+(y0)**2)))))
 momentum.append(m)
 energy.append(e)
 ######### First run velocity half step
 x_3 = np.power(np.sqrt(x0*x0 + y0*y0),3)

 vx0-=(x0*delta_t/2)/(x_3)   #v0 = v0-(-x0*dt/2) or v0 = v0+(a*dt/2)
 vy0-=(y0*delta_t/2)/(x_3)   #v0 = v0-(-x0*dt/2) or v0 = v0+(a*dt/2)
 
 print("\n")
 
 for j in range(nsteps):
     ######################## Main update: leapfrog algorithm
 
    x0+=vx0*delta_t  #Next position (x + v*dt) >> x next position
    y0+=vy0*delta_t  #Next position (x + v*dt) >> x next position
    
    x_3 = np.power(np.sqrt(x0*x0 + y0*y0),3)
    vx0-= (x0*delta_t)/x_3  #Next velocity
    vy0-= (y0*delta_t)/x_3  #Next velocity  
    t0+= delta_t

    
    momentum.append((x0*(vy0+y0*delta_t/(2*delta_t)))-(y0*(vx0+x0*delta_t/(2*delta_t))))
    energy.append((0.5*(vx0**2)+0.5*(vy0**2))-(1/np.sqrt((abs((x0**2)+(y0)**2)))))   
    x.append(x0)
    y.append(y0)
    vx.append(vx0+x0/x_3*delta_t/2)
    vy.append(vy0+y0/x_3*delta_t/2)
    t+=[t0]
   
   
    print("Step (" + str(j+1) + ") Conversation of energy:", ((0.5*(vx0**2)+0.5*(vy0**2))-(1/np.sqrt((abs((x0**2)+(y0)**2))))))
    print("Step (" + str(j+1) + ") Conversation of Angular Momentum:", (x0*vy0)-(y0*vx0))
    
 

 print("\n" + "Using the equation :  E = v^2 - 1/|x|, it is observed that energy is conserved")
 print("Using Anguluar Momentum: L = x1v2-x2v1, it is observed that the momentum is conserved as the algorithm is running")
 xarr=np.array(x) 
 yarr=np.array(y)
 vxarr=np.array(vx)
 vyarr=np.array(vy)
 tarr= np.array(t)

 fig, ax1 = plt.subplots(1)
 fig2, (ax2, ax3) = plt.subplots(2)

 ax1.plot(xarr, yarr, label=labels)
 ax1.set(xlabel='X Position', ylabel='Y Position', 
        title='Orbit trajectory')
 ax1.legend()
 fig.show()

 ax2.plot(tarr,[round(e,2) for e in energy])
 ax2.set(title = 'Energy vs Time')
 ax3.plot(tarr,[round(mo,5) for mo in momentum]) 
 ax3.set(title = 'Angular Momentum vs time')
 plt.ticklabel_format(useOffset=False)
 ax2.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
 ax3.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
 fig2.subplots_adjust(hspace = 0.9)

 fig2.show()
 plt.show()
 
 exit_seq()


#10, .1, 0 , .3, 10, 1000
