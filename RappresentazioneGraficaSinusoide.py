import matplotlib.pyplot as plt
import numpy as np
import math as m

V_max = float(input("Inserisci il/l' valore massimo/ampiezza della sinusoide: "))
angolo = float(input("Inserisci lo sfasamento della sinusoide in gradi: "))

f = 0.25 #freqeunza del segnale con T = 4 secondi
t = np.arange(0.0, 10.0, 0.01) # tempo
omega = 2*np.pi*f #pulsazione
phi = m.radians(angolo) #fase

y = V_max * np.sin((omega*t))

plt.plot(t, y)

plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=(phi/(np.pi/2)), color='k')
plt.show()