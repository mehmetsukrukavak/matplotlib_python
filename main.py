import random

import numpy as np
import matplotlib.pyplot as plt

age_list = np.array(random.sample(range(20,80),10))
weight_list = np.array(random.sample(range(70,120),10))


plt.plot(age_list, weight_list)
plt.xlabel("Age")
plt.ylabel("Weight")
plt.title("Age - Weight Graph")
plt.show()

