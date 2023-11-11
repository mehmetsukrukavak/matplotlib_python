import numpy as np
import matplotlib.pyplot as plt

np_numpy1 = np.linspace(0,15,20)
np_numpy2 = np_numpy1 ** 2

(myFig, myAxes) = plt.subplots()
myAxes.plot(np_numpy1, np_numpy2, "y*-")
myAxes.plot(np_numpy2, np_numpy1, "g--")

plt.show()


