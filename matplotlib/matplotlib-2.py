import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x, y, label='X Cubed')
axes[0].set_title('First Plot')

axes[1].plot(y,x, label='X Squared')
axes[1].set_title('Second Plot')

axes[0].legend(loc=0)
plt.tight_layout()
plt.show()
fig.savefig('my_picture.pdf')

