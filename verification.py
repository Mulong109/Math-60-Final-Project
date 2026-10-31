import numpy as np
import matplotlib.pyplot as plt

lamda = 1
n_sim = 1000
myList = []

for i in range(n_sim):
    u1 = np.random.uniform(0, 1)
    u2 = np.random.uniform(0, 1)
    u3 = np.random.uniform(0, 1)
    Y1 = - 1/lamda * np.log(1 - u1)
    Y2 = - 1/lamda * np.log(1 - u2)
    Y3 = - 1/lamda * np.log(1 - u3)
    M = min(Y1, Y2, Y3)
    myList.append(M)





M_values = np.array(myList)
x = np.linspace(0, M_values.max(), 400)
pdf_M = 3 * lamda * np.exp(-3 * lamda * x)

plt.hist(M_values, bins=30, density=True, alpha=0.6, edgecolor="black", label="Simulated M")
plt.plot(x, pdf_M, "r-", linewidth=2, label="Theoretical PDF: 3λe^(-3λx)")
plt.title("Histogram of M with Theoretical PDF")
plt.xlabel("M")
plt.ylabel("Density")
plt.legend()
plt.show()
