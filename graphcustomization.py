import numpy as np
import matplotlib.pyplot as plt

np_numpy1 = np.linspace(0,15,20)
np_numpy2 = np_numpy1 ** 3

plt.plot(np_numpy1, np_numpy2, "y*-")
plt.show()

plt.subplot(1, 2, 1)
plt.plot(np_numpy1, np_numpy2, "y*-")
plt.subplot(1, 2, 2)
plt.plot(np_numpy2, np_numpy1, "g--")
plt.show()
