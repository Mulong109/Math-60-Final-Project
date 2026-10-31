import numpy as np
import matplotlib.pyplot as plt

lamda = 1

u = np.random.uniform(0, 1, 100)

T = - 1/lamda * np.log(1 - u)

plt.hist(T, bins=20, edgecolor="black")
plt.title("Histogram of 100 samples of T")
plt.xlabel("T")
plt.ylabel("Frequency")
plt.show()
