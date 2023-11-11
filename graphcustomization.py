import numpy as np
import matplotlib.pyplot as plt

np_numpy1 = np.linspace(0,15,20)
np_numpy2 = np_numpy1 ** 2

plt.plot(np_numpy1, np_numpy2, "y*-")
plt.show()

my_figure = plt.figure()
my_axes = my_figure.add_axes([0.1,0.1,0.5,0.5])
my_axes.plot(np_numpy1,np_numpy2,"g*")
my_axes.set_xlabel("X Data")
my_axes.set_ylabel("Y Data")
my_axes.set_title("Graph Title")
plt.show()


my_figure2 = plt.figure()


my_axes3 = my_figure2.add_axes([0.1,0.1,0.9,0.9])
my_axes3.plot(np_numpy1, np_numpy2,"r*-")
my_axes3.set_xlabel("X Data Large")
my_axes3.set_ylabel("Y Data Large")
my_axes3.set_title("Large Graph")

my_axes2 = my_figure2.add_axes([0.25,0.4,0.3,0.3])
my_axes2.plot(np_numpy1, np_numpy2,"g*")
my_axes2.set_xlabel("X Data Small")
my_axes2.set_ylabel("Y Data Small")
my_axes2.set_title("Small Graph")

plt.show()

