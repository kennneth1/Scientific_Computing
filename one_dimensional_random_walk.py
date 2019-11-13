import random
import matplotlib.pyplot as plt
import numpy as np

def factorial(i):
    fac=1
    for j in range(1,i+1):
      fac*=j
    return fac

def prediction(time, position, p):
   x= (position+time)//2
   comb= factorial(time)/(factorial(x)*factorial(time-x))
   return (comb*((1-p)**x)*(p**(time-x)))

moves=(1,-1)

pos=0

n_part=int(input("Number of particles  "))
n_steps= int(input("Number of steps  "))
p=(float(input("Probability P: move left ")))
q = 1-p
         

pos=n_part*[0]
data=[]

for step in range(n_steps):
   data+=[tuple(pos)]
   for part in range(n_part):

       if random.uniform(0,1)<p:
           pos[part]-=1
       else:
           pos[part]+=1

data+=[tuple(pos)]


average_pos=sum(pos)/len(pos)
predicted_average = (1-(2*p))*n_steps
print("average position:", average_pos)
print("average position as defined by (1-2p)*nsteps:", predicted_average)

data=np.array(data)

data=np.transpose(data)

plt.figure()
    
plt.subplot(1,2,1)
for i in data[0:10]:
  plt.plot(i)
plt.xlabel("Random walk samples")

plt.subplot(1,2,2)
plt.xlabel("how many particles in the end")

xmin, xmax= min(pos), max(pos)
bin=((xmax-xmin)//2+1)*[0]
# print(pos)
#print(len(bin))

bins=list(range(xmin,xmax+1,2))
# print(bins)
for i in bins:
    bin[(i-xmin)//2]= pos.count(i)

#print(bins)
#print(bin)

plt.bar(bins,bin)
pred=[]

for i in bins:
  pred+= [n_part*prediction(n_steps,i,p)]


plt.plot(bins, pred, 'r')
tex = "Probability P = 0.33, " + "Number of particles = " + str(n_part) + ", Number of steps = " + str(n_steps) + "\n" + "Data's expected position: " + str(average_pos) + ", Actual expected position: " + str(round(predicted_average,2))
plt.suptitle(tex, fontsize = 7)

plt.show()

