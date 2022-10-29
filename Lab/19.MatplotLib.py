import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

p = [2, 3, 4, 5]
q = [20, 21, 31, 34]
plt.plot(p, q, label='Linear')
plt.show()
