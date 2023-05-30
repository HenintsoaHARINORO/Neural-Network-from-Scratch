import numpy as np

a = [1, 2, 3]
b = [2, 3, 4]

a = np.array([a])
b = np.array([b]).T
print(b)
print(a)
print(a.shape)

c = np.dot(a, b)
print(c)