import random
import matplotlib.pyplot as plt
from math import exp
import numpy as np
import math

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact = fact*i
    return fact

def decay(p):
    u=random.random()
    if u < p:
       return -1
    else:
       return 0


n_total=int(input("Total number of particles  "))
n_exp=float(input("particles that should decay in one unit of time "))
n_runs= int(input("Number of experiment runs  "))

prob= (n_exp/n_total)


def poisson(n):
    x = ((n_exp**n)/(factorial(n)))*(math.exp(-1*n_exp))
    return x


darr = []
for runs in range(n_runs): # Each experiment
    particles = [1]*n_total
    decay_count = 0
    for i in range(n_total):   # Each loop through the particles
        particles[i]=particles[i]+decay(prob)

    decay_count = particles.count(0)
    darr.append(decay_count)
    print("Experiment (" + str(runs) + ") Particles decayed: " + str(decay_count))

dist=[]
for i in range(min(darr),max(darr)):
    dist.append(n_runs*poisson(i))


binwidth = 0.5

plt.plot(list(range(min(darr),max(darr))), dist)
plt.hist(darr, bins=np.arange(min(darr), max(darr)+binwidth, binwidth))
plt.ylabel('Frequency')
plt.xlabel('Particles Decayed')
plt.show()


