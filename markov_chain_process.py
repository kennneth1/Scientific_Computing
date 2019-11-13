import random
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate

# Please make sure the Markovdata.txt file is in the same directory that you are reading this file from

wgen = ''
try:
    with open ('Markovdata.txt', 'rt') as f:
        for i in f:
            wgen+=i
except:
    print("No file found")
    f.close()

print(wgen)

p00_count = 0
p01_count = 0
p10_count = 0
p11_count = 0

for i in range(len(wgen)-1):
    if wgen[i] == '0' and wgen[i+1] == '0':
        p00_count+=1
    if wgen[i] == '0' and wgen[i+1] == '1':
        p01_count+=1
    if wgen[i] == '1' and wgen[i+1] == '0':
        p10_count+=1
    if wgen[i] == '1' and wgen[i+1] == '1':
        p11_count+=1

p00 = p00_count/(p00_count+p01_count)
p01 = p01_count/(p00_count+p01_count)
p10 = p10_count/(p10_count+p11_count)
p11 = p11_count/(p10_count+p11_count)

print('\n pij values -> p00:', p00, 'p01:', p01,'p10:', p10,'p11:', p11)

prob = np.linspace(0, 1,100)
L0= (p00_count*np.log(prob))+(p01_count*np.log(1-prob))
L1= (p10_count*np.log(prob))+(p11_count*np.log(1-prob))
y00 = L0.max()
x00 = prob[np.argmax(L0)]
y10 = L1.max()
x10 = prob[np.argmax(L1)]
print("Maximum likelihood for p00, p10:", [x00, x10])
print("Most likely values for p00, p10:", [p01, p10])

plt.plot(prob, L0, label='P00')
plt.plot(prob, L1, label='P10')
plt.xlabel('Probability')
plt.ylabel('Likelyhood L: ')
plt.legend()
plt.show()

z = np.array(prob)
L0 = np.array(L0)
L1 = np.array(L1)
ninf = float('-inf')
L0[L0 == ninf] = 0
L1[L1 == ninf] = 0

xi, yi = np.linspace(z.min(), z.max(), 100), np.linspace(z.min(), z.max(), 100)
xi, yi = np.meshgrid(z, z)
rbf = scipy.interpolate.Rbf(L0, L1, z, function='linear')
zi = rbf(xi, yi)
plt.imshow(zi, vmin=z.min(), vmax=z.max(), origin='lower',extent=[L0.min(), L0.max(), L1.min(), L1.max()])
plt.scatter(L0, L1, c=z)
plt.colorbar()
plt.show()

file2= open("Markovdata.txt",'w')
for w in wgen:
    file2.write(str(w))
file2.close()


exit()
