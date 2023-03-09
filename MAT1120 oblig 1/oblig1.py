import numpy as np 
import matplotlib.pyplot as plt

def sirkel(x,y,r):
    #lager en array fra 0 - 2pi med 100 i mellomrom
    t = np.linspace(0, 2*np.pi, 100)
    #plotter x aksen og y aksen med 2 i tykkelse
    plt.plot(x + r*np.cos(t), y + r*np.sin(t), linewidth = 1)
    plt.axis("equal")

#disse lager matrisene, uncomment den du vil se og comment de du ikke vil se
#3a
#A = np.array([[-2, 0, 1/2, 1], [-1/4, 1, 1/4, 0], [0, 0, 3, -1], [1/8, 1/8, 1/4, 2]])

#3b
#A = np.array([[5, 1, 1], [1, 2, 1], [1, -1, -1]])

#3c
#A = np.array([[-2, 0, 1/2, 1, 2], [-1/4, 1, 1/4, 0, 5], [0, 0, 3, -1, 7], [1/8, 1/8, 1/4, 2, 4], [4, 3, 8, 6, 4]])

#3d
A = np.array([[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]])


#lager en 4 lang array med 0 inni, denne inneholder d_j
x = np.zeros(len(A))

#lager en 4 lang array med 0 inni, denne er for radiusen
r = np.zeros(len(A))

#forloop for å finne d_jj
for y in range(len(A)): #00 01 02 03
    #fyller x med verdier fra arrayen diagonalt
    x[y] =  A[y][y]
    #forloop for å summere
    for z in range(len(A)):
        #adderer verdien fra hvert av kolonnene fra A til r
        r[y] = r[y] + abs(A[y,z])
    #tar r og substraherer y fra den
    r[y] = r[y]-abs(x[y])
    z = 0

#for hver x
for y in x:
    sirkel(x[z], 0, r[z])
    z += 1

#bruker eig() som returnerer egenverdi og egenvektor for en matrise
egenverdi, egenvektor = np.linalg.eig(A)

#for loop for plotting
for teller in range(len(egenverdi)):
    #lager dottene
    plt.plot(np.real(egenverdi[teller]), np.imag(egenverdi[teller]), '.', markersize = 20)

#viser plotten
plt.show()
