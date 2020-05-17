import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])

# Can also enter RG hex code
ax.plot(x, y, color='orange', lw=0.75, alpha=0.8, ls='-.', marker='x', ms=10,
        mfc='black')

ax.set_xlim([0,1])
ax.set_ylim([0,2])
plt.show()
