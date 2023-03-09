#oppgave1,2
import numpy as np 
import matplotlib.pyplot as plt
from numpy import linalg as LA
"""tall = int(input("skriv n matrise"))
list2 = []
teller = 1
while teller <= tall:
    teller +=1
    list1 = []
    teller2 = 1
    while teller2 <= tall:
        teller2 +=1
        inn = float(input("skriv en verdi"))
        list1.append(inn)
    list2.append(list1)"""
def sirkel(x,y,r):
        t = np.linspace(0,2*np.pi,100)
        plt.plot(x+r*np.cos(t),y+r*np.sin(t),linewidth=2)
        plt.axis("equal")

def matrix():
    A = np.array([[-2, 0, 1/2, 1], [-1/4, 1, 1/4, 0], [0, 0, 3, -1], [1/8, 1/8, 1/4, 2]])
    x = np.zeros(len(A))
    r = np.zeros(len(A))
    for y in range(len(A)): 
        x[y] =  A[y][y]
        for z in range(len(A)):
            r[y] = r[y] + abs(A[y,z])
        r[y] = r[y]-abs(x[y])
    z = 0
    for y in x:
        sirkel(x[z],0,r[z])
        z +=1
    print(A)
    print(np.shape(A))
    egenverdi, egenvektor = np.linalg.eig(A)
    print(egenverdi)
    teller = 0
    while (teller < len(egenverdi)):
        plt.plot(np.real(egenverdi[teller]),
                np.imag(egenverdi[teller]), '.', markersize=30)
        teller += 1
    plt.show()
matrix()

#

