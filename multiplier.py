import numpy as np


res = 0
for i in range(100):
    mat1 = np.random.randn(1000, 1000)
    mat2 = np.random.randn(1000, 1000)

    res += np.sum((mat1 @ mat2).flatten())

print ('Mat output: ', res)