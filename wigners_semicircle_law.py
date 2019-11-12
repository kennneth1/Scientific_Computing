import numpy as np
import matplotlib.pyplot as plt
import cmath
from numpy import linalg as LA


#For each component of the matrix, generate two Gaussian distributed
# numbers (with width 1), to be the real and imaginary part of the component of the matrix M.

def print_matrix(n):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in n]))

def random_matrix(s):
    matrix = []
    for x in range(s):
        row = []
        for y in range(s):
            mu, sigma = 0, 1 # mean and standard deviation
            a = np.random.normal(mu, sigma, 1)
            b = np.random.normal(mu, sigma, 1)
            z = complex(a, b)
            z = round(z.real, 4) + round(z.imag, 4) * 1j
            row.append(z)
        matrix.append(row)
    h_matrix = (np.matrix(matrix)).getH()
    w_matrix = h_matrix+np.matrix(matrix)
    w, v = LA.eigh(h_matrix+w_matrix)
    return w.tolist()

eigen_30 = []
eigen_100 = []
for i in range(0,100):
    eigen_30.append(random_matrix(30))
    eigen_100.append(random_matrix(100))

eigen_30 = [y for x in eigen_30 for y in x]  #Nd Array containing all eigenvalues (with their components)
eigen_100 = [y for x in eigen_100 for y in x]


fig = plt.figure(2,(15,5))
fig.suptitle('Semi-circle Law for 2 Matrices')
plt.subplot(1,2,1)
bins, vals, patches = plt.hist(eigen_30, bins=100)
H = max(bins)
R = max(abs(vals))
x = np.linspace(-R,R,100)
y = np.array([H*np.sqrt(1-(xval/R)**2) for xval in x])
plt.plot(x,y, color = 'r', linewidth = 2)
plt.xlabel('Eigenvalues')
plt.ylabel('N: Probability Density')
plt.title('Histogram for the Eigenvalues of 100 30x30 Matrices  ')

plt.subplot(1,2,2)
bins, vals, patches = plt.hist(eigen_100, bins=200)
H = max(bins)
R = max(abs(vals))
x = np.linspace(-R,R,100)
y = np.array([H*np.sqrt(1-(xval/R)**2) for xval in x])
plt.plot(x,y, color = 'r', linewidth = 2)
plt.xlabel('Eigenvalues')
plt.ylabel('N: Probability Density')
plt.title('Histogram for the Eigenvalues of 100 30x30 Matrices  ')
plt.show()
plt.savefig('q2_plots.png')