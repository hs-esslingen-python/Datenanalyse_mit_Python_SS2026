# https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html

import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

# Select an backend
# More information about backends: https://matplotlib.org/stable/users/explain/backends.html
#matplotlib.use('Qt5Agg')

fig, ax = plt.subplots()
ax.plot(t, s,label=r"Label: 1 + $\sin(2 \cdot \pi \cdot t)$")
ax.set_xlabel('X-Achse - Zeit [s]')
ax.set_ylabel('Y-Achse - Spannung [V]')
ax.set_title('Überschrift oberhalb des Bildes')
ax.grid(True)
ax.legend()

print("Saving figure to test.png")
print("Current working directory: ", os.getcwd())

fig.savefig(r".\test.png")

plt.show()
#plt.show(block=True)
#plt.interactive(False)
